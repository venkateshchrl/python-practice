maxNo = int(input("Enter No. of Fibonacci to be printed: "))

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


fibonacciList = []
for i in range(1, maxNo+1):
    fibonacciList.append(fibonacci(i))

print(fibonacciList)