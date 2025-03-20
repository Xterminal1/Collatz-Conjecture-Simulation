def isEven(n):
    return n % 2 == 0

def collatz(n):
    o = n
    if isEven(n): 
        return True
    while n != 1:
        if n < o: 
            return True
        if not isEven(n): 
            n = n * 3 + 1
        else: 
            n /= 2
        if n == o: 
            return False
    return True

n = int(input('n: '))
check = collatz(n)
print(f'PASSED!') if check else print(f'FAILED!')
