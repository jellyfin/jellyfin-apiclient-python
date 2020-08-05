# This is based on https://github.com/jellyfin/jellyfin-web/blob/master/src/components/syncPlay/timeSyncManager.js
import threading
import logging
import datetime

LOG = logging.getLogger('Jellyfin.' + __name__)

number_of_tracked_measurements = 8
polling_interval_greedy = 1
polling_interval_low_profile = 60
greedy_ping_count = 3


class Measurement:
    def __init__(self, request_sent, request_received, response_sent, response_received):
        self.request_sent = request_sent
        self.request_received = request_received
        self.response_sent = response_sent
        self.response_received = response_received

    def get_offset(self):
        """Time offset from server."""
        return ((self.request_received - self.request_sent) + (self.response_sent - self.response_received)) / 2.0

    def get_delay(self):
        """Get round-trip delay."""
        return (self.response_received - self.request_sent) - (self.response_sent - self.request_received)

    def get_ping(self):
        """Get ping time."""
        return self.get_delay() / 2.0


class _TimeSyncThread(threading.Thread):
    def __init__(self, manager):
        self.manager = manager
        self.halt = threading.Event()
        threading.Thread.__init__(self)

    def run(self):
        while not self.halt.wait(self.manager.polling_interval):
            try:
                measurement = self.manager.client.jellyfin.utc_time()
                measurement = Measurement(measurement["request_sent"], measurement["request_received"],
                                          measurement["response_sent"], measurement["response_received"])

                self.manager.update_time_offset(measurement)

                if self.manager.pings > greedy_ping_count:
                    self.manager.polling_interval = polling_interval_low_profile
                else:
                    self.manager.pings += 1

                self.manager._notify_subscribers()
            except Exception:
                LOG.error("Timesync call failed.", exc_info=True)

    def stop(self):
        self.halt.set()
        self.join()


class TimeSyncManager:
    def __init__(self, client):
        self.ping_stop = True
        self.polling_interval = polling_interval_greedy
        self.poller = None
        self.pings = 0  # number of pings
        self.measurement = None  # current time sync
        self.measurements = []
        self.client = client
        self.timesync_thread = None
        self.subscribers = set()

    def is_ready(self):
        """Gets status of time sync."""
        return self.measurement is not None

    def get_time_offset(self):
        """Gets time offset with server."""
        return self.measurement.get_offset() if self.measurement is not None else datetime.timedelta(0)

    def get_ping(self):
        """Gets ping time to server."""
        return self.measurement.get_ping() if self.measurement is not None else datetime.timedelta(0)

    def update_time_offset(self, measurement):
        """Updates time offset between server and client."""
        self.measurements.append(measurement)
        if len(self.measurements) > number_of_tracked_measurements:
            self.measurements.pop(0)

        self.measurement = min(self.measurements, key=lambda x: x.get_delay())

    def reset_measurements(self):
        """Drops accumulated measurements."""
        self.measurement = None
        self.measurements = []

    def start_ping(self):
        """Starts the time poller."""
        if not self.timesync_thread:
            self.timesync_thread = _TimeSyncThread(self)
            self.timesync_thread.start()

    def stop_ping(self):
        """Stops the time poller."""
        if self.timesync_thread:
            self.timesync_thread.stop()
            self.timesync_thread = None

    def force_update(self):
        """Resets poller into greedy mode."""
        self.stop_ping()
        self.polling_interval = polling_interval_greedy
        self.pings = 0
        self.start_ping()

    def server_date_to_local(self, server):
        """Converts server time to local time."""
        return server - self.get_time_offset()

    def local_date_to_server(self, local):
        """Converts local time to server time."""
        return local + self.get_time_offset()

    def subscribe_time_offset(self, subscriber_callable):
        """Pass a callback function to get notified about time offset changes."""
        self.subscribers.add(subscriber_callable)

    def remove_subscriber(self, subscriber_callable):
        """Remove a callback function from notifications."""
        self.subscribers.remove(subscriber_callable)

    def _notify_subscribers(self):
        for subscriber in self.subscribers:
            try:
                subscriber(self.get_time_offset(), self.get_ping())
            except Exception:
                LOG.error("Exception in subscriber callback.")
