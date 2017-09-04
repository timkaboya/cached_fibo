cached_fibo
===========

Step 1: 
===========
Determine the nth Fibonacci number using both iterative and recursive techniques.
Program is fibo.py
This works fine with low numbers but is slow in calculating fibo numbers above 40.
Slows to a crawl for those over 100.

Step 2: 
===========
Determine nth Fibonacci number using memoization technique

Program uses Memoization to determine even higher fibonacci numbers.
    
For higher fibo numbers, take adv of memoization instead of searching them directly
    Ex: Finding 1000th fibo number directly will cause recursion depth problem 
    but searching for 300, 500, 750 then 1000 will give you needed result.

    When u search starting from lower, the lower fibo values are cached.
