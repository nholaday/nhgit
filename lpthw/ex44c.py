class Parent(object):
    def modify(self):
        print "PARENT modify()"

class Child(Parent):
    def modify(self):
        print "CHILD modify() before super"
        super(Child, self).modify()
        print "CHILD modify() after super"
        
dad = Parent()
son = Child()

dad.modify()
son.modify()
