# scaling.py
import threading
import time

class AutoScaler:
    def __init__(self):
        self.lock = threading.Lock()
        self.max_resources = 10
        self.current_resources = 1

    def scale_up(self):
        with self.lock:
            if self.current_resources < self.max_resources:
                self.current_resources += 1
                print(f"Scaled up to {self.current_resources} resources")

    def scale_down(self):
        with self.lock:
            if self.current_resources > 1:
                self.current_resources -= 1
                print(f"Scaled down to {self.current_resources} resources")

    def monitor(self):
        while True:
            # Example condition for scaling
            if self.current_resources < self.max_resources:
                self.scale_up()
            time.sleep(10)  # Check every 10 seconds

# Example usage
if __name__ == "__main__":
    scaler = AutoScaler()
    threading.Thread(target=scaler.monitor).start()
