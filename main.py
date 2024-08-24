import matplotlib.pyplot as plt 
import numpy as np
import time

def collatz(param):
    global numbers
    iterations, max_number, number = 0, 0, param
    numbers = []
    while number != 1: 
        if number > max_number:
            max_number = number
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1
        iterations += 1
        numbers += [number]
    return iterations, int(max_number)

while 1:
    print('----------------------------------------------------------')
    print('|            Collatz Conjecture Simulation               |')
    print('----------------------------------------------------------')
    print()
    
    number = input('Input an integer to be tested: ')
    if number.lower() == 'exit':
        break

    try:
        number = int(number)
        start_time = time.time()
        iterations, max_number = collatz(number)

        print()
        print(f'N: {number}')
        print(f'Iterations: {iterations}')
        print(f'Highest N: {max_number}')

        if number > 10**54:
            number = '{:e}'.format(number)
        plt.title(f'Collatz Conjecture Simulation | N: {number}')
        plt.xlabel(f'Iterations ({iterations})')
        if max_number > 10**54:
            max_number = '{:e}'.format(max_number)
        plt.ylabel(f'Numbers (Highest: {max_number})')
        ypoints = np.array(numbers)
        plt.plot(ypoints, marker = '.')
        plt.show()
        
        end_time = time.time()
        elapsed = end_time - start_time
        print(f'({elapsed:.8f} seconds)')
        print()

    except ValueError:
        print(f'Invalid input. Enter an integer.')
