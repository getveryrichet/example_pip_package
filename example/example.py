import numpy as np
# after from example import example
# allows using example.child_example.child_example() 
from .child import child_example 

def hello_requests():
    print(np)

def check_time():
    child_example.child_example_time()