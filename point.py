from __future__ import annotations
import math

class Point:
    def __init__(self, x: int, y: int):
        '''create two-dimensional point (x,y)'''
        self.x = x
        self.y = y

    def translate(self, dx: int, dy: int) -> None:
        '''Move this point dx horizontally and dy vertically'''
        self.x = self.x + dx
        self.y = self.y + dy

    def distance(self, other_point: Point) -> float:
        '''Return distance between this point and other_point'''
        a = (other_point.x - self.x) ** 2
        b = (other_point.y - self.y) ** 2
        return math.sqrt(a + b)
    
    def __repr__(self) -> str:
        '''Return x, y coordinates of point as (x, y)'''
        return f'({self.x}, {self.y})'
    
    def __lt__(self, other_point: Point) -> bool:
        '''Return Ture if this point and other_point are of
           type Point and x, y of this point is less than the 
           x, y of other_point'''
        return isinstance(other_point, Point) and self.x < other_point.x and self.y < other_point.y
    
# Main program
p1 = Point()
print(f'({p1.x},{p1.y})')
p1.translate(3, 7)
print(f'({p1.x},{p1.y})')

p2 = Point(5, 6)
print(p1.distance(p2))

print('p1 <? p2:', p1 < p2)
print('p2 <? p1:', p2 == p1)    