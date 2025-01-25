def isDistinct(x: int) -> bool:
    s = str(x)
    digits_used = []
    for i in s:
        if i in digits_used:
            return False
        digits_used.append(i)
    return True

x = int(input("Enter your number: "))
x += 1
while not isDistinct(x):
    x += 1
print(x)
