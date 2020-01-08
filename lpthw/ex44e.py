class Other(object):

    def override(self):
        print "Other override()"

    def implicit(self):
        print "Other implicit()"

    def modify(self):
        print "Other modify()"

class Child(object):
    
    def __init__(self):
        self.other = Other()

    def override(self):
        self.other.override()

    def implicit(self):
        self.other.implicit()

    def modify(self):
        print "Child before modify"
        self.other.modify()
        print "Child after modify"

thing = Other()
daughter = Child()

thing.implicit()
daughter.implicit()

thing.override()
daughter.override()

thing.modify()
daughter.modify()
