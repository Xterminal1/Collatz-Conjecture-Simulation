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
n = int(input('n:              '))
start = time.time()

steps, evenSteps, oddSteps, max = collatz(n)

print(f'({len(str(n))} digits)')
print(f'steps:          {steps}')
print(f'even steps:     {evenSteps}')
print(f'odd steps:      {oddSteps}')

if oddSteps == 0:
    print(f'even-odd:       ~')
else:
    print(f'even-odd:       {evenSteps/oddSteps:.8f}')

if evenSteps == 0:
    print(f'odd-even:       ~')
else:
    print(f'odd-even:       {oddSteps/evenSteps:.8f}')

print(f'peak:           {max} ({len(str(max))} digits)')

if n == max:
    print(f'n=peak:         TRUE')
else:
    print(f'n=peak:         FALSE')

end = time.time()
run_time = end - start
print(f'time:           {run_time:.5f}s\n')
