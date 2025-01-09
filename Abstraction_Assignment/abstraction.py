# Import the necessary modules
from abc import ABC, abstractmethod

# Define abstract class as a child of ABC
class Animal(ABC):
    # Create abstract method, using the '@abstractmethod' decorator
    # It won't do anything and can't be used yet
    @abstractmethod
    def make_sound(self):
        pass

    #Regular method
    def sleep(self):
        print("Zzzz...")

# We then create classes as children of the abstract class,
# each utilizing the abstract method differently
class Dog(Animal):
    def make_sound(self):
        print("Bark!")

class Cat(Animal):
    def make_sound(self):
        print("Meow?")

# This class will cause an error if used because it doesn't define the
# abstract method from the parent class
class Fish(Animal):
    def swim(self):
        print("Swimming...")


dog = Dog()
dog.make_sound() # This will output 'Bark!'
dog.sleep()      # This will output 'Zzzz...'

cat = Cat()
cat.make_sound() # This will output 'Meow?'
cat.sleep()      # This will output 'Zzzz...'

# These, as stated above, will cause an error
# fish = Fish()
# fish.swim()

# This will also cause an error, because you can't instantiate an abstract class
# animal = Animal()
