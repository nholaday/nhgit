## Animal is-a object (yes, sort of confusing )look at the exra credit.
class Animal(object):
    pass

## Dog is-a type of Animal
class Dog(Animal):

    def __init__(self,name):
        ## Dog has-a __init__ with variable name
        self.name = name

## class Cat is an Animal
class Cat(Animal):

    def __init__(self,name):
        ## Cat has-a init with variable name
        self.name = name

## class Person is-a object
class Person(object):

    def __init__(self,name):
        ## Person has-a init method with variable name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a init method with attribute super
        super(Employee, self).__init__(name)
        ## Employee has-a init method with attribute salary
        self.salary = salary

## class Fish is-a object
class Fish(object):
    pass

## class Salmon is-a Fish
class Salmon(Fish):
    pass

## class Halibut is-a Fish
class Halibut(Fish):
    pass

## set rover to an instance of Dog.  rover is-a Dog
rover = Dog("Rover")

## satan is-a instance of Cat
satan = Cat("Satan")

## mary is-a instance of Person
mary = Person("Mary")

## mary has-a attribute pet set it equal to satan
mary.pet = satan

##  duder is-a instance of Employee
duder = Employee("Duder", 120000)

## duder has-a attribute pet, set it to rover
duder.pet = rover

## flipper is-a instance of Fish
flipper = Fish()

## crouse is-a instance of Salmon
crouse = Salmon()

## harry is-a instance of Halibut
harry = Halibut()

print "mary.pet = ", mary.pet.name
print "flipper = ", flipper
