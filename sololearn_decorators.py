
def decor1(func):
    def wrap(*args, **kwargs):
        print "---------------"
        func(*args, **kwargs)
        print "---------------"
    return wrap

@decor1
def adder(x,y):
    print(x + y)

#adder(2,3)

#this is the same as doing this
def adder2(x,y):
    print (x+x+y)

adder2 = decor1(adder2)
adder2(2,3)

@decor1
def multiplier(x,y):
    print(x * y)

multiplier(2,3)