# @classmethods can be used as an alternative contructor to __init__ when
# the arguements are a different type

class AddList(object):
    def __init__(self, numlist):
        self.sum = 0
        for item in numlist:
            self.sum += item

    @classmethod
    def from_string(cls,str):
        convertedtolist = str.split(',')
        intlist = []
        for item in convertedtolist:
            intlist.append(int(item))
        return cls(intlist)

numbers = [1,3,5,7,8]
# AddList normally takes a list as an arguement
al = AddList(numbers)
print al.sum

# say the arguement is a comma separated string
numberstring = "1,3,5,7,8"
al2 = AddList.from_string(numberstring)
print al2.sum
