lst = input().split()
n = int(lst[0])
m = int(lst[1])

items = set()
for i in range(n):
    items.add(int(input()))
completed_assignments = 0

for i in range(n):
    num_items = int(input())
    assignment = set()
    for j in range(num_items):
        assignment.add(input())
    if assignment.issubset(items):
        completed_assignments += 1

print(completed_assignments)