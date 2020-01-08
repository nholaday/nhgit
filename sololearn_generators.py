# A function can be turned into a generator by using yield
# a generator an 'iterable' similar to a list or tuple
# yield acts like return, but instead of ending the function, it pauses it and
# saves the state.  When called again it will continue from the last yield

def evens():
    i = 0
    while i < 15:
        yield i
        i += 2

# access elements in the generator with 'for' statements
for a in evens():
    print a

def printfirst():
    li = [(1,3),(5,9),(6,2),(1,5)]
    i = 0
    while i < len(li):
        yield li[i][0]
        i += 1

pf = printfirst()
pf2 = printfirst()
print(next(pf))
print(next(pf))
print(next(pf))
print(next(pf))
# or call with a for loop
for p in printfirst():
    print p
    
# Generators can be created on the fly with generator expressions
# They look a lot like list comprehensions
lc = [x**3 for x in range(1,5)]
ge = (x**3 for x in range(1,5))
print lc
print ge
print(next(ge))   
print(next(ge))   
print(next(ge))   
print(next(ge))   
