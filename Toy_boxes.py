'''
We are given n unopened toy boxes with k number of of figurines in each box.
The boxes can not be opened and hence, the order of the figurines can not be
changed. A box can not rotated (otherwise the figurines will be facing the
wrong way)

Each figurines is specified by its height. For example, in a given box the
height of the figurin from left to right 4, 5 and 7.
Note that the number of figurines in each box may vary.

We would like to organize all the toy boxes such that they are arranged in
non-decreasing order of figurine heights from left right.
However, this may not necessarily be possible with the given boxes. Hence, 
write a program to determine if we can have such an arrangement or not.

Input specification:
First line of input: integer n representing the number of toy boxes
Next n lines: one for each box. Each of these lines begin with:
    - Integer k indicating the number of figurines in the box (k >= 1)
    - Followed by k integers giving the height of figurines from left to right
      separated by a space.
      Each height is an integer value >= 1.

Output specification:
Yes, if we can organize the boxes.
No, otherwise.
'''

'''
Top-Down Design: Capturing the main tasks of your solution
- Some tasks will not require much code.
  - Will solve them directly.
- Other tasks will require more from us.
  - Will define a function.
'''

# TODO: Read the input
# TODO: Check if all boxes are sorted
# TODO: Obtain a new list of boxes with only the left and right heights
# TODO: Sort the boxes (i.e. the intervals)
# TODO: Determine whether the boxes are organized or not
# TODO: Output the result

def readBoxes(n):
    lst_boxes = []
    for i in range(n):
        box = input().split()
        box.pop(0)
        for i in range(len(box)):
            box[i] = int(box[i])
        lst_boxes.append(box)
    return lst_boxes

def allBoxesOK(lst_boxes):
    for box in lst_boxes:
        if box != sorted(box):
            return False
    return True

def boxIntervals(lst_boxes):
    intervals = []
    for box in lst_boxes:
        intervals.append([box[0], box[-1]])
    return intervals

def allIntervalsOK(lst_intervals):
    prev_max_height = lst_intervals[0][1]
    for box in range(1, len(lst_intervals)):
        curr_min_height = lst_intervals[box][0]
        if curr_min_height < prev_max_height:
            return False
        prev_max_height = lst_intervals[box][1]
    return True

n = int(input('Enter the number of toy boxes: '))
boxes = readBoxes(n)

if not allBoxesOK(boxes):
    print('No')
else:
    intervals = boxIntervals(boxes)
    intervals.sort()
    if allIntervalsOK(intervals):
        print('Yes')
    else:
        print('No')