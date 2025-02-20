laundary = 0
lst = input("Input 1: ").split()
lst_2 = input("Input 2: ").split()
for i in range(len(lst)):
    lst[i] = int(lst[i])

for i in range(len(lst_2)):
    lst_2[i] = int(lst_2[i])

n = int(lst[0])
m = int(lst[1])
d = int(lst[2])
x = n

for i in range(d):
    if i in lst_2: 
        n += 1
        x += 1
    if n == 0:
        laundary += 1
        n = x
    n -= 1
    
print(laundary)

