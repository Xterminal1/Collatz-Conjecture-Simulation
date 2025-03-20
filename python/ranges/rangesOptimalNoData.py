import time

def collatz(n):
    orig = n
    while n != 1:
        if n % 2 != 0:
            n = (n * 3 + 1) / 2
        else:
            n /= 2
        if n < orig:
            break

min = 3
limit = int(input('Limit: '))
start = time.time()

for i in range(min, limit + 1, 2):
    collatz(i)
    if i % (limit/100) == 1:
       print(f'{i-1}: PASSED')

# for i in range(1, limit + 1):
#     collatz(i)
#     print(f'{i}: PASSED')

end = time.time()
elapsed = end - start
print(f'Time: {elapsed:.4f}s')
