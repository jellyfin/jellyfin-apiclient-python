import threading

class KeepAlive(threading.Thread):
    def __init__(self, timeout, ws):
        self.trigger        = threading.Event()
        self.halt           = False
        self.timeout        = timeout
        self.ws             = ws

        threading.Thread.__init__(self)
    
    def stop(self):
        self.halt = True
        self.join()

    def run(self):
        force_next = False
        while not self.halt:
            if self.trigger.wait(self.timeout/2):
                if self.halt:
                    break
            else:
                self.ws.send("KeepAlive")
