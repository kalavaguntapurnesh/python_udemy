import threading
import time

def prepare_chai(type_, wait_time):
    print(f"{type_} chai: Brewing....")
    time.sleep(wait_time)
    print(f"{type_} chai: ready")


t1 = threading.Thread(target=prepare_chai, args=("Masala", 2)) # creating thread
t2 = threading.Thread(target=prepare_chai, args=("Ginger", 3))

t1.start()
t2.start()

t1.join()
t2.join()

