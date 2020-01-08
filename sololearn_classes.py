import random

class Animal(object):
    '''
    Here is the docstring for class Animal
    '''
    # __init__ method is called when creating an instance of the class
    # The __init__ method is called the class constructor
    def __init__(self, name):
        # when an instance is created, the argument will be stored as its name
        # for example rover.name = "Rover Cleaveland"
        self.name = name
        self.food = 0
        print "Creating a new animal with name %s" % name

    def speak(self):
        print "Hi, I am a --%s--!" % self.type

    def eat(self):
        self.food += 10
        print self.name, "eats <('o')>"


class Cat(Animal):
    '''
    This class inherits all methods and variables from Animal
    '''
    # redefinining th __init__ method will overwrite the super's(parent's)
    def __init__(self, name):
        #you can call the super's function however using super()
        super(Cat,self).__init__(name)
        self.type = "cat"


class Dog(Animal):
    '''
    This class also inherits all methods and variables from Animal
    '''
    # defining a method with the same name as in the super(parent) class
    # overrides the super's method
    def speak(self):
        print "Ruff Ruff!"

# Creating instances(objects) of the Cat and Dog class blueprints
fiesty = Cat("Fiesty McFiester")
rover = Dog("Rover Cleaveland")
spot = Dog("Spot Hammond")

animallist = [fiesty,rover,spot]
for ani in animallist:
    ani.speak()
    for i in range(0,random.randint(0,3)):
        ani.eat()
    print ani.food

print ""
