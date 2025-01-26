def decide_flow():
    if ans == 99:
        percentage = int(input("Enter the percentage of the flow: "))
        split = index * (percentage / 100)
        split_2 = index - split
        nums_flow.pop(nums_river)
        nums_flow.insert((nums_river), split_2)
        nums_flow.insert((nums_river + 1), split)
    elif ans == 88:
        join = nums_flow[nums_river] + nums_flow[nums_river + 1]
        nums_flow.pop(nums_river)
        nums_flow.pop(nums_river)
        nums_flow.insert(nums_river, join)

inital_stream = int(input("Enter the inital number of streams: "))
nums_flow = []
infinite_loop = 0

for i in range(inital_stream):
    flow = int(input("Enter the flow of the each stream from left-to-right: "))
    nums_flow.append(flow)

while(infinite_loop == 0):
    ans = int(input("Enter 77, 88 or 99:"))
    if ans != 77:
        nums_river = int(input("Enter the number of the river: ")) - 1
        index = nums_flow[nums_river]
        decide_flow()
    else:
        print(nums_flow)
        exit()