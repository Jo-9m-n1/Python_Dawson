from pet import Pet
from mammal import Mammal
from herbivore import Herbivore

class Bunny(Mammal, Herbivore, Pet):
    def __init__(self, legs = 4, ears = 2):
        super().__init__(legs)
        self.ears = ears

    def __repr__(self) -> str:
        result = 'Species: Bunny'
        result = Mammal.__repr__(self) + result
        result += '\n' + Pet.__repr__(self)
        return result + '\n' + Herbivore.__repr__(self)
    
    def reproduce(self) -> None:
        result = "Bunnies can produce multiple littres per year"

        print(super().reproduce() + '\n' + result)

    def move(self) -> str:
        print("I move by hopping and I can see behind me")

    def sleep(self):
        print("Bunnies as nocturnal animals, typically sleep around 12 to 14 hours.")

    def eat(self) -> None:
        Herbivore.eat(self)
        print("I mostly eat fresh grass.")
    
    def pet(self):
        print("You can pet this animal!")

if __name__ == '__main__':
    b = Bunny()

    print()
    b.__repr__()

    print()
    b.reproduce()
    b.eat()
    b.sleep
    b.pet()