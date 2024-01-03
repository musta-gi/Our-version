import time 

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Function {func.__name__} took {end-start} for execution')
        return result
    return wrapper

# Use example
@timeit
def main():
    L = [i for i in range(1000000)]
    print(f'Length of list is {len(L)}')
    return None

if __name__ == '__main__':
    main()