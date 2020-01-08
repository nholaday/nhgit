# use s.find() and s.rfind() to find the leftmost instance of a string
# it then returns the first index of that string

s = "I don't want a large Farva, I want a liter of cola!"
print(s.find("wan",0,len(s)))
print(s.rfind("wan",0,len(s)))