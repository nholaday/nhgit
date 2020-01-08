# methods and variables in classes can't be strictly locked
# but their use can be discouraged when appropriate

class BaseClass(object):
    def __init__(self, passedlist):
        # putting a _ is a 'weak' hide.  It signals that it
        # should not be accessed but is not enforced
        # It does not import with 'from file import *'
        self._hiddenlist = passedlist

    def printlist(self):
        print self._hiddenlist

    # strongly hidden variables have double underscores
    # to access them you need _classname__variable
    __secretcode = 333

    def __printcode(self):
        print self.__secretcode

base = BaseClass([5,6,9,10])
print base._hiddenlist
base.printlist()

print base._BaseClass__secretcode
base._BaseClass__printcode()
try:
    print base.__secretcode
except:
    print "Unable to print secretcode"

base.__printcode()
