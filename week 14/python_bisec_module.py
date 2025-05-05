'''
--> lst to work with
--> num want to insert
--> [start, end] interval of the kst to consider
(default to the entre list)

>>> import bisect
>>> lst = [1, 2, 7, 7, 7, 8, 10, 11]
>>> num = 7
>>> bisect(lst, num, start, end)
5

returns the index where num can be inserted into lst sort that lst sorted
if num already in the lst, return rightmost index where num can be inserted

>>> bisect_left(lst, num, start, end)
>>> 2

returns the index where num can be inserted into lst sort that lst sorted
it num already in lst, returns leftmost index where num can be inserted

>>> bisect_right(lst, num, start, end)  # bisect_right is the same as bisect
5
'''

import bisect
lst = [1, 2, 7, 7, 7, 8, 10, 11]
num = 7

print(bisect.bisect(lst, num)) 
print(bisect.bisect_right(lst, num))
print(bisect.bisect_left(lst, num))  