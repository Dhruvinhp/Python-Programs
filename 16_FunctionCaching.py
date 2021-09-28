import time
from functools import lru_cache

@lru_cache(maxsize=3) #store last 3 operation
def work(n): 
    time.sleep(n)
    return n

if __name__ == "__main__":
    print("Security breach...")
    work(3)
    print("bracking......25%")
    work(3) # not perform sleep operation
    print("bracking......50%")
    work(3) 
    print("bracking......75%")
    work(3)
    print("bracking......100%")
    print("Successfully breach complete! ")