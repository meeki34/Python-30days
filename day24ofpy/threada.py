import threading
import time


# name = "example_module"
# print('Output:', name)
# print('Thread:', threading.current_thread().name)

def func(x):
    time.sleep(x)
    if not threading.current_thread() is threading.main_thread():
        print(f"Thread {threading.current_thread().name} is running")
t = threading.Thread(target=func, args=(2,), name="MyThread")
t.start()

print(threading.main_thread())
print("Main Thread")


def fun(y):
    print("Current Thread Details:", threading.current_thread().name)
    for i in range(y):
        print("Internal Thread Running:", i)
        print("Internal thread finished")

t = threading.Thread(target=fun, args=(5,), name="InternalThread")
t.start()

for i in range(5):
    print("Main Thread Running:", i)
print("Main thread finished")