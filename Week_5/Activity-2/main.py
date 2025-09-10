from horse import Horse
from parrot import Parrot   
# Main function to demonstrate the classes
def main():
    # Create an instance of Horse
    horse = Horse(gender="Male", color="Brown", breed="Thoroughbred")
    print(horse.info())
    horse.make_sound()
    horse.move()

    # Create an instance of Parrot
    vocabulary = ["Hello!", "Power Learn Project", "Want a cracker", "Python is fun!", "I love coding!", "Goodbye!"]
    parrot = Parrot(gender="Female", color="Green", vocabulary=vocabulary)
    print(parrot.info())
    parrot.make_sound()
    parrot.move()
    parrot.say_word()
if __name__ == "__main__":
    main()