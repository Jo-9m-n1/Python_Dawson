class Empty(Exception):
    '''Error attempting to access an element from an empty container'''
    pass
class Stack:
    def __init__(self):
        self.__data = []

    def __len__(self) -> int:
        '''return length of stack'''
        return len(self.__data)
    
    def isEmpty(self) -> bool:
        '''return True if stack is empty, False otherwise'''
        return len(self.__data) == 0
    
    def push(self, elem: object) -> None:
        ''''add element elem to the top of the stack
        >>> s = Stack()
        >>> s.push(5)
        >>> s.push(3)
        >>> s.pop()
        3
        '''
        self.__data.append(elem)

    def top(self):
        '''return (but do not remove) the element at the top of the stack'''
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self.__data[-1] 
    
    def pop(self):
        '''remove the element at the top of a stack and return its value'''
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self.__data.pop()
    
    def __repr__(self) -> str:
        return ' '.join(map(str, self.__data))
    
if __name__ == '__main__':
    print(8, '|   |')