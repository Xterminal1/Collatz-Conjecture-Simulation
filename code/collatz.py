import time

def collatz(param):
    global numbers
    iterations, max_number, number = 0, 0, param
    while number != 1: 
        if number > max_number:
            max_number = number
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1
        iterations += 1
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
        
        end_time = time.time()
        elapsed = end_time - start_time
        print(f'({elapsed:.8f} seconds)')
        print()

    except ValueError:
        print(f'Invalid input. Enter an integer.')
