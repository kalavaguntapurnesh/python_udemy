import threading

def task():
    for i in range(3):
        print(threading.current_thread().name, i)


t1 = threading.Thread(target=task, name="Thread 1")
t2 = threading.Thread(target=task, name="Thread 2")

t1.start()
t2.start()


t1.join()
t2.join()


#we created 2 threads and asked them to run concurrently
# But GIL, will make only run one thread at a time