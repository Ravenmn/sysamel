import threading

class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while True:
            # philosopher is thinking
            print(f"{self.name} is thinking.")
            # philosopher picks up left fork
            self.left_fork.acquire()
            print(f"{self.name} picked up the left fork.")
            # philosopher picks up right fork
            self.right_fork.acquire()
            print(f"{self.name} picked up the right fork.")
            # philosopher is eating
            print(f"{self.name} is eating.")
            # philosopher puts down right fork
            self.right_fork.release()
            print(f"{self.name} put down the right fork.")
            # philosopher puts down left fork
            self.left_fork.release()
            print(f"{self.name} put down the left fork.")

if __name__ == "__main__":
    forks = [threading.Lock() for n in range(5)]
    philosophers = [Philosopher(f"Philosopher {n}", forks[n], forks[(n+1)%5]) for n in range(5)]
    for p in philosophers:
        p.start()