import threading

class KeepAlive(threading.Thread):
    def __init__(self, timeout, ws):
        self.halt           = threading.Event()
        self.timeout        = timeout
        self.ws             = ws

        threading.Thread.__init__(self)
    
    def stop(self):
        self.halt.set()
        self.join()

    def run(self):
        while not self.halt.is_set():
            if self.halt.wait(self.timeout/2):
                break
            else:
                self.ws.send("KeepAlive")
