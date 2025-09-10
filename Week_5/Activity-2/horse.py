from animal import Animal
class Horse(Animal):
    """
        A class representing a horse, inheriting from the Animal class.

        Attributes:
            breed (str): The breed of the horse.
    """
    def __init__(self, gender: str = "", color: str = "", breed: str = ""):
        super().__init__(gender, color)
        self.__breed = breed

    # Getter
    @property
    def breed(self):
        return self.__breed

    # Setter
    @breed.setter
    def breed(self, breed: str):
        self.__breed = breed

    # Method to get horse's details
    def info(self):
        return f"**** Horse Details ****\n{super().info()}\nBreed: {self.__breed}"

    # Override make_sound method
    def make_sound(self):
        print("The horse is neighing...")

    # Override move method
    def move(self):
        print("The horse gallops gracefully........................")
