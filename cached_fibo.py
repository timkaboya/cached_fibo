""" 
    Program to generate requested fibonacci number. 
    Program uses Memoization to determine even higher fibonacci numbers. 

    For higher fibo numbers, take adv of memoization instead of searching them directly
    Ex: Finding 1000th fibo number directly will cause recursion depth problem
    but searching for 300, 500, 750 then 1000 will give you needed result
"""

# Method to cache execution and make program execute faster
def cached_execution(cache, proc, proc_input):
    if proc_input not in cache:
        cache[proc_input] = proc(proc_input)
    return cache[proc_input]


def cached_fibo(n):
    assert n > -1

    if n == 0 or n == 1:
        return n
    else:
        return cached_execution(cache, cached_fibo, n-1) + \
                cached_execution(cache, cached_fibo, n-2)

def main():

    while True:
        print(cached_fibo(int(input('Which Fibonacci number do you want: '))))


if __name__ == '__main__':
    cache = {} #initial cache to store computed fibo numbers. 
    main()

