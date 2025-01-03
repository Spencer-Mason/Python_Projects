#First we define a general animal class
class Animal:
    arms = None
    legs = None

    #Most animals make sound, different animals will define thier own speaking
    def speak(self):
        pass

#Create a human class as a child of animal
class Human(Animal):
    name = "Finn"
    arms = 2
    legs = 2
    thumbs = True

    def speak(self):
        print("Hello, I am a human.")

#Create a dog class as a child of animal
class Dog(Animal):
    name = "Jake"
    color = "yellow"
    legs = 4
    tail = True

    def speak(self):
        print("Dog! Dog!... I mean, Bark! Bark!")
