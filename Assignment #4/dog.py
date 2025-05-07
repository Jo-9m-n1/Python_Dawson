from pet import Pet
from mammal import Mammal
from omnivore import Omnivore

class Dog(Mammal, Omnivore, Pet):
    def __init__(self, legs = 4, ears = 2):
        super().__init__(legs)
        self.ears = ears

    def __repr__(self) -> str:
        result = 'Species: Dog'
        result = Mammal.__repr__(self) + result
        result += '\n' + Pet.__repr__(self)
        return Omnivore.__repr__(self)+ '\n' + result
    
    def reproduce(self) -> None:
        result = "Dogs can reproduce litter of puppies"

        print(super().reproduce() + '\n' + result)

    def move(self) -> str:
        print("I move by walking")

    def sleep(self):
        print("I sleep 12 hours a day")

    def eat(self) -> None:
        Omnivore.eat(self)
        print("I eat anything I can find")

    def pet(self):
        print("You can pet this animal!")

if __name__ == '__main__':
    d = Dog()

    print()
    d.__repr__()
    d.reproduce()
    d.eat()
    d.sleep
    d.pet()

    print()
    d.eat()

    print()
    d.pet()