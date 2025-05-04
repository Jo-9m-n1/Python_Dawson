'''
Implement a custom iterator class to generate 
even numbers in the interval [start, end]
'''

class EvenNumbers:
    def __init__(self, start, end, current = 0):
        self.start = start
        self.end = end
        self.current = current

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            if self.current % 2 == 0:
                result = self.current
                self.current += 1
                return result
            else:
                self.current += 1
                return self.__next__()
            
e = EvenNumbers(1, 11)
print(list(e))

'''
Implement a custom iterable class for the Fibonacci
numbers.  This class constructor should take n, 
representing the first n terms of the Fibonacci 
sequence
'''

class Fibonacci:
    def __init__(self, n):
        self.term = n
        self._count = 0
        self._prev, self._current = 0, 1

    def __iter__(self):
         return self

    def __next__(self):
        while self._count <= self.term:
            self._count = 1
            result = self._prev
            self._prev, self._current = self._current, self._current + self._prev
        return result

y = Fibonacci(5)
print(list(y))

'''
Draw the recursion tree for the computation of 
recSum(10)
'''



'''
write a recursive function that determines the
minimum element in a given list of integers. 
'''


'''
write a recursive function that converts a string of integers
into its integer counterpart
'''

'''
write a recursive function to determine if a given string
is a palindrome
'''

'''
Write a recursive function to count number of vowels in a string
'''

'''
use recursion to determine if a string has more vowels than consonants. 
'''