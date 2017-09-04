"""
    This program generates the requested fibonacci number. 
    Note that this program will run for long if the requested fib number is quite high.
    Ex: 300th Fibonacci number
    This program does not utilize any memory optimization techniques and serves to demonstrate memoization in tandem with the other program
"""

# Recursive Fibo
def fibo_r(n):
    assert n > -1

    if n == 0 or n == 1:
        return n
    else:
        return fibo_r(n-1) + fibo_r(n-2)

# Iterative Fibo
def fibo_i(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b
def main(): 
    while True:
        print (fibo_i(int(input('Which fibonacci number do you want: '))))


if __name__ == '__main__':
    main()
