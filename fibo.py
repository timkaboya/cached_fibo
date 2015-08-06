"""
    This program generates the requested fibonacci number. 
    Note that this program will run for long if the requested fib number is quite high.
    Ex: 300th Fibonacci number
    This program does not utilize any memory optimization techniques and serves to demonstrate that in tandem with the other program
"""


def fibo(n):
	if n == 0 or n == 1:
		return n
	else:
        for i in range(n):
			n = i + n
		return n
     
            
#TODO
# Recursive Algorithm for later. 

def main(): 
	while True:
		print (fibo(int(input('Which fibonacci number do you want: '))))
		

if __name__ == '__main__':
	main()
