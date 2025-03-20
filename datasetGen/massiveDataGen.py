# printed data can be customizable
# such as odd-even ratios, steps, peaks, etc.

import time
import csv
import os

def collatz(n):
    steps, oddSteps, evenSteps, max = 0, 0, 0, 0
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

def createFile(start, end):
    fileName = f"collatz_{start}_{end}.csv"
    if not os.path.exists(fileName):  # Check if file exists
        with open(fileName, "w") as file:  # Create the file
            pass
    return fileName

xpoints = []

def run(start, end):
    fileName = createFile(start, end)
    with open(fileName, "w", encoding="UTF8", newline="") as f:
        header = ["n", "steps", "even steps", "odd steps", "odd-even ratio", "max", "n=max?"]
        writer = csv.writer(f)
        writer.writerow(header)
        for n in range(start, end + 1):
            steps, evenSteps, oddSteps, max_val = collatz(n)
            isMax = (n == max_val)
            if evenSteps == 0:
                ratio = "~"
            else:
                ratio = f"{oddSteps/evenSteps:.5f}"
                ratio = float(ratio)
            writer.writerow([n, steps, evenSteps, oddSteps, ratio, max_val, isMax])
            xpoints.append(ratio)
        
        print(xpoints)

if __name__ == '__main__':
    lLimit = 1
    uLimit = 100_000
    run(lLimit, uLimit)


""""""
