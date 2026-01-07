import threading
import time

def brew_chai():
    print(f"[{threading.current_thread().name}] Starting to brew chai...")
    count = 0
    for _ in range(100_000_000):
        count += 1  # Simulate CPU-bound work
    print(f"[{threading.current_thread().name}] finished to brew chai...")

threading1 = threading.Thread(target=brew_chai, name="Thread-1")
threading2 = threading.Thread(target=brew_chai, name="Thread-2")

start = time.time()

threading1.start()
threading2.start()

threading1.join()
threading2.join()

end = time.time()
print(f"Total time taken: {end - start:.2f} seconds")
# Note: Due to Python's Global Interpreter Lock (GIL),
# the threads will not run in true parallel for CPU-bound tasks.
# This means the total time taken will be close to the sum of the times taken by each thread.
# This demonstrates that threading in Python may not improve performance for CPU-bound tasks.
# Instead, consider using multiprocessing for CPU-bound tasks to achieve true parallelism.
