from point import Point
class Segment:
    '''line segments'''
    def __init__(self, p1: Point, p2: Point):
        '''Create a segment between p1 and p2'''
        self.p1 = p1
        self.p2 = p2
    
    def translate(self, dx: int, dy: int) -> None:
        '''Move segment by dx horizontally and dy vertically'''
        self.p1.translate(dx, dy)
        self.p2.translate(dx, dy)
    
    def length(self) -> float:
        '''Return length of segment'''
        return self.p1.distance(self.p2)
    
    def __lt__(self, other_segment: Segment) -> bool:
        self.length() < other_segment.length()
# Main program
p1 = Point(2, 5)
p2 = Point(4, 2)

line1 = Segment(p1, p2)