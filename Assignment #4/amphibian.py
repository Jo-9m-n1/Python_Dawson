from animal import Animal

class Amphibian(Animal):
    def reporduce(self) -> str:
        result = "Amphibians reproduce by laying soft eggs in the water."

        return super().reproduce() + result
    
    def __repr__(self) -> str:
        return super().__repr() + '\nClass: Mammal'