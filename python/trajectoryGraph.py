import matplotlib.pyplot as plt 
import numpy as np
import time
import math

def collatz(n):
    i, max = 0, 0
    pts = [math.log10(n)] # LOG 10 to show differences at small and large scales
    while n != 1: 
        if n > max:
            max = n
        if n % 2 == 0:
            n //= 2 # used // rather than / bc % uses floating-point arithmetic
        else:
            n = n*3 + 1
        i += 1
        pts += [math.log10(n)]
        #pts += [n]
    return i, max, pts

while 1:
    print('----------------------------------------------------------')
    print('|            Collatz Conjecture Simulation               |')
    print('----------------------------------------------------------\n')
    
    n = input('Input an integer to be tested: ')
    if n.lower() == 'exit':
        break

    try:
        n = int(n)
        start = time.time()
        i, max, pts = collatz(n)

        print(f'\nN: {n}')
        print(f'Iterations: {i}')
        print(f'Highest N: {max}')

        if n > 10**54:
            n = '{:e}'.format(n)
        if max > 10**54:
            max = '{:e}'.format(max)
        
        plt.title(f'Collatz sequence trajectory (log10)', None, 'left')
        plt.title(f'N: {n} | Iterations: {i} | Max: {max}', None, 'right')
        plt.xlabel(f'Iterations')
        plt.ylabel(f'Number reached')
        ypoints = np.array(pts)
        plt.plot(ypoints, marker = '.')
        plt.show()
        
        end = time.time()
        run_time = end - start
        print(f'({run_time:.8f} seconds)')
        print()

    except ValueError:
        print(f'Invalid input. Enter an integer.')

#75128138247
