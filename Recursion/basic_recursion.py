def iterSum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def recSum(n):
    if n == 1:
        return 1
    else:
        return n + recSum(n - 1)

def recFactorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recFactorial(n - 1)
    
def badFibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return badFibonacci(n - 1) + badFibonacci(n - 2)
    
def goodFibonacci(n):
    pass

