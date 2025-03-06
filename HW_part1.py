'''
Given a dictionary of keys that are strings and/or integers,
values are lists, write asnippet of code that returns total 
number of elements of all lists that have keys as strings

Example:
d = {3: [3, 6], 'a': [3, 4, 5], 'b': [7, 8, 91, 1]}
Prints out a 7
'''

d = {3: [3, 6], 'a': [3, 4, 5], 'b': [7, 8, 91, 1]}
num = 0
for key in d:
    if type(key) == str:
        num += len(d[key])
print(num)


'''
Write a function wordTally that takes an integer argument n
and reads n words from the user. Note that the user may enter
the same word multiple times.
Your function should tally up how many times each words occurs
that the user has entered and store it in a dictionary where the 
keys are the words and the values are the number of times each word
occurs.
Return this dictionary.

You may create only one collection, namely the dictionary to be returned.
'''

def wordTally(n):
    d = {}
    for i in range(1, n + 1):
        word = input(f'Write your word #{i}: ')
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d
print(wordTally(3))

'''
Example:
d = {3: 5, 4: 5, 6: 1}
d_inverted = {5: [3, 4], 1: [6]}
'''

d = {3: 5, 4: 5, 6: 1}
d_inverted = {}
for key,value in d.items():
    if value not in d_inverted:
        d_inverted[value] = []
    d_inverted[value].append(key)
print(d_inverted)