from heterotroph import Heterotroph

class Herbivore(Heterotroph):
    def eat(self):
        super().eat()
        print("I eat plants")

    def __repr__(self) -> str:
        result = "This organism is herbivore, it feeds on plant matter its physiology facilitates food search"

        return super().__repr() + result