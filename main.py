import matplotlib.pyplot as plt
import numpy as np
import time

def Collatz_conjecture(n): # Test number input
    i = 0 # Number of iterations
    nums = [n]
    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        i += 1
        nums.append(n)
    
    print(n)
    i += 1
    return i, nums

while 1:
    print('------------------------------------------')
    print('|     Xterminal1 : Collatz Simulation    |')
    print('------------------------------------------')
    print()

    print('Input an integer to be tested:')

    num = input('>>> ')

    if num.lower() == 'exit':
        break

    try:
        num = int(num)
        start_time = time.time()

        iterations, nums = Collatz_conjecture(num)
        max_num = max(nums)

        print()
        print(f'Iterations: {iterations}')
        print(f'Highest number: {max_num}')
        
        # Matplotlib Graphing
        if num > 10**54:
            num = '{:e}'.format(num)
        plt.title(f'Collatz Conjecture Simulation | n = {num}')
        plt.xlabel(f'Iterations = {iterations}')
        if max_num > 10**54:
            max_num = '{:e}'.format(max_num)
        plt.ylabel(f'Numbers | Highest Number = {max_num}')
        ypoints = np.array(nums)
        plt.plot(ypoints, marker = '.')
        plt.show()

        end_time = time.time()
        elapsed = end_time - start_time
        print(f'({elapsed:.8f} seconds)')
        print()

    except ValueError:
        print(f'Invalid input. Enter an integer.')
