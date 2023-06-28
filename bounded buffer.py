import threading
import time

class BoundedBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def put(self, item):
        with self.not_full:
            while len(self.buffer) == self.capacity:
                self.not_full.wait()
            self.buffer.append(item)
            print(f'Put: {item}')
            time.sleep(1)  # Simulate some processing time
            self.not_empty.notify()

    def get(self):
        with self.not_empty:
            while len(self.buffer) == 0:
                self.not_empty.wait()
            item = self.buffer.pop(0)
            print(f'Got: {item}')
            time.sleep(1)  # Simulate some processing time
            self.not_full.notify()
            return item

# Example usage
buffer = BoundedBuffer(5)

def producer():
    for i in range(10):
        buffer.put(i)

def consumer():
    for i in range(10):
        item = buffer.get()

# Create and start the producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)
producer_thread.start()
consumer_thread.start()

# Wait for both threads to finish
producer_thread.join()
consumer_thread.join()