x = int(input())
y = []

for i in range(x):
    y.append(int(input()))
y.sort()

sizes = []
for i in range(1, x - 1):
    a = (((y[i + 1] - y[i]) / 2) + y[i]) 
    b = (((y[i] - y[i - 1]) / 2) + y[i - 1])
    c = a - b
    sizes.append(c)


sizes.sort()
print(sizes[0])