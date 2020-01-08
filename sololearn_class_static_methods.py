# class methods can be called on the class itself instead of an instance of the class
# you can call the class's method with creating an instance(object) of the class
class Squared(object):
    def __init__(self, num):
        self.square = num ** 2

    def printsquare(self):
        print self.square

    @classmethod
    def addthensquare(cls, a, b):
        return cls(a+b)

    # static methods can be called by the class itself instaed of an instance of the class too
    # the difference is that static methods don't return an instance of the class
    # they just behave like a normal function

    @staticmethod
    def addten(c):
        # the self arg is not needed because self refers to the instance of the class
        return c+10

squared1 = Squared(4)
print squared1.square
squared1.printsquare()

squared2 = Squared.addthensquare(2,3)
print squared2.square
squared2.printsquare()

num1 = Squared.addten(7)
print num1
