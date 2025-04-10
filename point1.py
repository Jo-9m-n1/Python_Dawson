class Point:
    def __init__(self):
        '''create two-dimensional point (0,0)'''
        self.x = 0
        self.y = 0

    def __init__(self, x: int, y: int):
        '''create two-dimensional point (x,y)'''
        self.x = x
        self.y = y
        
# Main program
p1 = Point()
print(f'({p1.x},{p1.y})')