from pet import Pet
from bird import Bird
from omnivore import Omnivore

class Parrot(Bird, Omnivore, Pet):
    def __init__(self, legs = 2, wings = 2, colour = 'yellow'):
        super().__init__(legs)
        self.wings = wings
        self.colour = colour

    def __repr__(self) -> str:
        result = 'Species: Parrot'
        result = Bird.__repr__(self) + result
        result += '\n' + Pet.__repr__(self)
        return result + '\n' + Omnivore.__repr__(self)
    
    def reproduce(self) -> None:
        result = "Parrots often take a few days to lay a full clutch of eggs. This can be as many as three to four eggs"

        print(super().reproduce() + '\n' + result)

    def eat(self) -> None:
        Omnivore.eat(self)
        print("I eat both plant and animal matter. My natural diet includes a variety of foods like seeds, nuts, fruits, vegetables, flowers, buds, and insects.")

    def move(self) -> str:
        print("I can walk in various ways. I can fly, walk, climb and even use a unique method called 'beakiation' to traverse nasrrow branches.")

    def sleep(self) -> str:
        print("Parrots sleep around 10 to 12 hours each night, often tucked under their wings. They amy also take naps during the day.")
    
    def pet(self) -> str:
        print("You can pet this animal!")

if __name__ == '__main__':
    p = Parrot()

    p.__repr__()
    p.reproduce()
    p.eat()
    p.sleep
    p.pet()
