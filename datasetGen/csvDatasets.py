import time
from os.path import basename
from sys import argv
import csv

start_time = time.time()

def current_time():
    return time.time() - start_time

def seconds(value):
    return value - (minutes(value) * 60) - (hours(value) * 3600)

def minutes(value):
    return int(value / 60) - (hours(value) * 60)

def hours(value):
    return int(value / 3600)

def formatted_time(value):
    return "%02d:%02d:%02d" % (hours(value), minutes(value), seconds(value))

def console_message(message):
    source = "[%s][%s]: " % (formatted_time(current_time()), basename(argv[0]))
    print(source + message)

# If input n is even, divide by 2
# If input n is odd, multiple by 3 and then add 1
def collatz(n: int) -> int:
    if n >= 0:
        if n % 2 == 0:
            return int(n / 2)
        else:
            return (3 * n) + 1
    else:
        console_message("ERROR: Input value cannot be less than 0!")
        return -1

# Returns how many iterations of collatz conjecture it takes to reach one from the input n value.
def collatz_to_one(n: int, step=0) -> int:
    if n == 0:
        return n
    if n < 0:
        return -1
    if n == 1:
        return step
    else:
        return collatz_to_one(collatz(n), step + 1)

# Creates new file, as well as returns the string for the file name
# Name of file is based on number range generated, and for multiple files in the same range, generates new name
def create_new_file(start, length):
    console_message("Attempting to create new file.")

    file_name = "collatz_" + str(start) + "_" + str(length + start - 1) + "_"
    file_ext = ".csv"
    valid_name = False
    attempts = 1
    full_file_name = ""

    while not valid_name:
        full_file_name = file_name + "(" + str(attempts) + ")" + file_ext
        try:
            file = open(full_file_name, "x")
        except IOError:
            attempts += 1
        else:
            valid_name = True

    return full_file_name

# Starting with x = "start", returns first n = "length" numbers,
# the next value when applying the rules of the collatz conjecture,
# and the number of steps before reaching 1 using the collatz conjecture.
# Stores values in generated .csv file
def run_collatz(start, length):
    console_message("Running collatz conjecture for numbers " + str(start) + " through " + str(start + length - 1))

    file_name = create_new_file(start, length)
    with open(file_name, "w", encoding="UTF8", newline="") as f:
        header = ["number", "next", "steps_to_one"]

        writer = csv.writer(f)

        writer.writerow(header)

        for n in range(length):
            num = n + start
            next = collatz(n + start)
            steps = collatz_to_one(n + start)

            writer.writerow([num, next, steps])
            
            
if __name__ == '__main__':
    console_message("Starting program.")

    size = 1000000
    initial = 0
    for x in range(1):
        run_collatz((x * size) + 1 + initial, size)
