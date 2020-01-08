class Parent(object):

    def modify(self):
        print "PARENT modify()"

    def implicit(self):
        print "PARENT implicit()"

    def override(self):
        print "PARENT override()"

class Child(Parent):
    def modify(self):
        print "CHILD modify() before super"
        super(Child, self).modify()
        print "CHILD modify() after super"

    def override(self):
        print "PARENT override()"
        
dad = Parent()
son = Child()

dad.implicit()
son.implicit()
dad.override()
son.override()
dad.modify()
son.modify()
