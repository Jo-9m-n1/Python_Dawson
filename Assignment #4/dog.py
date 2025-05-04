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
        return result + '\n' + Omnivore.__repr__(self)
    
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

if __name__ == '__main__':
    d = Dog()

    print()
    d.reproduce()

    print()
    d.move()

    print()
    d.sleep

    print()
    d.eat()