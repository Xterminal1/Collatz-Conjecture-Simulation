import time
import sys

def collatz(n):
    steps = 0
    oddSteps = 0
    evenSteps = 0
    max = 0
    while n != 1: 
        if n > max: 
            max = n
        if n % 2 == 0: 
            n //= 2
            evenSteps += 1
        else: 
            n = n * 3 + 1
            oddSteps += 1
        steps += 1
    return steps, evenSteps, oddSteps, max

sys.set_int_max_str_digits(1_000_000)

lLimit = int(input('limit 1:              '))
uLimit = int(input('limit 2:              '))

if uLimit > lLimit:
    nums = range(lLimit, uLimit + 1)

    for n in nums:

        print(f'n:              {n}')
        steps, evenSteps, oddSteps, max = collatz(n)

        print(f'steps:          {steps}')
        print(f'even steps:     {evenSteps}')
        print(f'odd steps:      {oddSteps}')

        if oddSteps == 0:
            print(f'steps ratio:    ~')
        else:
            print(f'steps ratio:    {evenSteps/oddSteps:.5f}')

        print(f'peak:           {max} ({len(str(max))} digits)')

        if n == max:
            print(f'n=peak:         TRUE')
        else:
            print(f'n=peak:         FALSE')

        print()
