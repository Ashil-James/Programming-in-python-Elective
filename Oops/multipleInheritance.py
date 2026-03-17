class Father:
    def __init__(self, fname):
        self.fname = fname
        print("Father constructor")

class Mother:
    def __init__(self, mname):
        self.mname = mname
        print("Mother constructor")

class Child(Father, Mother):
    def __init__(self, fname, mname, cname):
        super().__init__(fname)   # calls Father constructor
        Mother.__init__(self, mname)  # manually call Mother
        self.cname = cname
        print("Child constructor")

c = Child("John", "Mary", "Alex")