class Animal:
    """
        A class representing an animal.
        
        Attributes:
            gender  (str): The gender of the animal.
            color   (str): The color of the animal.

        Methods:
            make_sound(): Prints a sound specific to the animal.
            move()      : Prints a message indicating the animal is moving.
            info()      : Returns a string with the animal's details.
    """
    def __init__(self, gender : str = "", color : str = ""):
        self.__gender = gender
        self.__color = color

    # Getters
    @property
    def gender(self):
        return self.__gender

    @property
    def color(self):
        return self.__color
    
    # Setters
    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @color.setter
    def color(self, color: str):
        self.__color = color

    # Method animal's behavior
    def make_sound(self):
        print(f"The animal makes a sound.")

    # Method animal's movement
    def move(self):
        print(f"The animal moves on all fours.")

    # Method to get animal's details
    def info(self):
        return f"\nGender: {self.__gender} \nColor: {self.__color}"