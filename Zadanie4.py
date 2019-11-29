import time
from random import randint

ranger = 1000000
long_list = [randint(0, 3000) for element in range(ranger)]

timer_start = time.perf_counter()
for x in range(ranger):
    if long_list == (-1):
        print("-1 found!")

timer_stop = time.perf_counter()
timer_total = timer_stop - timer_start
print("Timer start: ", timer_start)
print("Timer end: ", timer_stop)
print("Timer reading: ", timer_total)

timer_start = time.perf_counter()
if (-1) not in long_list:
    print("-1 is not on the list")
else:
    print("-1 found!")
timer_stop = time.perf_counter()
print("Timer start: ", timer_start)
print("Timer end: ", timer_stop)
print("Timer reading: ", timer_total)