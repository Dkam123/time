import time
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("Please wait...")
time.sleep(3)
print("Your time for function: ")

start_time = time.perf_counter()


print(fibonacci(15))
end_time = time.perf_counter()


print(f"The execution time {end_time - start_time:.8f} seconds")

start_time = time.perf_counter()

print(fibonacci(15))
end_time = time.perf_counter()

print(f"The execution time {end_time - start_time:.8f} seconds")