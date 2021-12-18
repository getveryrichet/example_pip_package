import numpy as np 
import time

def child_example():
    print("child example", np) 

#to check whether time package can be used by process which doesn't import time package
def child_example_time():
    print("time package", time)
