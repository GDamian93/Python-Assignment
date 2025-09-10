from animal import Animal
class Parrot(Animal):
    """
        A class representing a parrot, inheriting from the Animal class.

        Attributes:
            vocabulary (list): A list of words the parrot can say.

        Methods:
            say_word(): Prints a random word from the parrot's vocabulary.
    """
    def __init__(self, gender: str = "", color: str = "", vocabulary: list = None):
        super().__init__(gender, color)
        self.__vocabulary = vocabulary if vocabulary is not None else []

    # Getter
    @property
    def vocabulary(self):
        return self.__vocabulary

    # Setter
    @vocabulary.setter
    def vocabulary(self, vocabulary: list):
        self.__vocabulary = vocabulary

    # Method to get parrot's details
    def info(self):
        return f"**** Parrot Details ****\n{super().info()}\nVocabulary: {', '.join(self.__vocabulary)}"

    # Override make_sound method
    def make_sound(self):
        print("The parrot is squawking...")

    # Override move method
    def move(self):
        print("The parrot is flying gracefully.")

    # Method for the parrot to say a word from its vocabulary
    def say_word(self):
        if self.__vocabulary:
            import random
            word = random.choice(self.__vocabulary)
            print(f"The parrot says: {word}")
        else:
            print("The parrot has no words to say.")