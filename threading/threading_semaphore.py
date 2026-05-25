import threading
import time

# Create a semaphore that allows a maximum of 3 threads to access the resource at once
connection_limit = threading.Semaphore(3)

def access_database(client_id):
    print(f"Client {client_id} is waiting to connect...")
    
    # Acquire the semaphore. If 3 threads are already inside, others will block/wait here.
    with connection_limit:
        print(f"===> Client {client_id} CONNECTED! (Lock acquired)")
        # Simulate doing some database operations (takes 2 seconds)
        time.sleep(2)
        print(f"<=== Client {client_id} finished work and disconnected.")
    
    # The lock is automatically released here when exiting the 'with' block

# Spawn 7 clients trying to access the database
threads = []
for i in range(1, 8):
    t = threading.Thread(target=access_database, args=(i,))
    threads.append(t)
    t.start()
    # Tiny pause between starting threads just to make the console prints print nicely
    time.sleep(0.1)

# Wait for all threads to finish
for t in threads:
    t.join()

print("All database requests processed!")
