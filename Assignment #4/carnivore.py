from heterotroph import Heterotroph

class Carnivore(Heterotroph):
    def eat(self):
        super().eat()
        print("I eat meat")

    def __repr__(self) -> str:
        result = "This organism is carnivore. It feeds on other animals, and its physical features facilitate hunting."
        return super().__repr() + result