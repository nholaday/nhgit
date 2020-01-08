class Namefun(object):

    def createName(self, name):
        self.name = name

    def returnName(self):
        return self.name
    
    def printName(self):
        print self.name

firstinst = Namefun()
secinst = Namefun()

firstinst.createName("Tula")
firstinst.printName()
print "Here is the name returned: %s" % firstinst.returnName()
