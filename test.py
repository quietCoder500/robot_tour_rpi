from functools import wraps
from time import sleep


def time_it(func):
 import time
 @wraps(func)
 def wrapper(*args,**kwargs):
  start = time.time()
  result = func(*args,**kwargs)
  print(f'time taken by {func.__name__} is {time.time()-start }')

  return result
 return wrapper

@time_it
def fib(num):
    print(f'Calculating fib({num})')
    sleep(0.5)
print(fib(700000))