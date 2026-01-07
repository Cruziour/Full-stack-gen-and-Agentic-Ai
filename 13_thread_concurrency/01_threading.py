import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(1)  # Simulate time taken to take an order

def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai for order #{i}")
        time.sleep(2)  # Simulate time taken to brew chai

# create threads for taking orders and brewing chai
order_thread = threading.Thread(target=take_orders)
chai_thread = threading.Thread(target=brew_chai)

# start the threads
order_thread.start()
chai_thread.start()

# wait for both threads to complete
order_thread.join()
chai_thread.join()

print("All orders taken and chai brewed!")
