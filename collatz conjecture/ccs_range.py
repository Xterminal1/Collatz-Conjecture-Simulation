import matplotlib.pyplot as plt
import numpy as np

def collatz(param):
    iterations, max_number, number = 0, 0, param
    while number != 1: 
        if number > max_number:
            max_number = number
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1
        iterations += 1
    return iterations, max_number

print('----------------------------------------------------------')
print('|            Collatz Conjecture Simulation               |')
print('----------------------------------------------------------')
print()

low_bound = int(input('Input the lower bound: '))
high_bound = int(input('Input the higher bound: '))

if high_bound > low_bound:
    total_max_number = 0
    numbers = range(low_bound, high_bound + 1)
    iterations_list = []
    highest_number_list = []

    for n in numbers:
        print()
        print(f'N: {n}')
        iterations, max_number = collatz(n)
        print(f'Iterations: {iterations}')
        print(f'Highest N: {max_number}')
        iterations_list.append(iterations)
        highest_number_list.append(max_number)

    plot1 = plt.subplot(1, 2, 1)
    plt.title(f'Comparing seed numbers and their iteration times')
    plt.xlabel('Numbers')
    plt.ylabel('Iterations')
    plt.plot(numbers, iterations_list, '.')

    plot2 = plt.subplot(1, 2, 2)
    plt.title('Comparing seed numbers and their highest numbers reached')
    plt.xlabel('Numbers')
    plt.ylabel('Highest Number')
    plt.plot(numbers, highest_number_list, '.')
    plt.show()
else:
    print('Invalid input. The higher bound should be larger than the lower bound.')
