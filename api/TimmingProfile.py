import time

class TimingProfile:
    def __init__(self, write_delay=0.0, soft_delay=0.0, query_delay=0.0):
        self.write_delay = write_delay
        self.soft_delay = soft_delay
        self.query_delay = query_delay

    def sleep_write(self):
        if self.write_delay > 0:
            time.sleep(self.write_delay)

    def sleep_query(self):
        if self.query_delay > 0:
            time.sleep(self.query_delay)

    def delay(self):
        if self.soft_delay > 0:
            time.sleep(self.soft_delay)
