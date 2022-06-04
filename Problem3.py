#- Look around your classroom or your bedroom and come up with 3 classes that you see 
#there. 
#- For each class define 3 instance Variables
#- For each class define 1 static variable
#- For each class define an accessor and a mutator for each instance variable
#- For each class define 2 instance methods in addition to the accessors and the mutators.
#- For each class define a constructor which initializes all its instance variables. 

class Class1:
    def __init__(self, one, two, three):
        self._one = one
        self._two = two
        self._three = three
    
    @staticmethod
    def staticMtd_class1(one, second):
         one = one

    def setclass1_mutators(self, one, two, three):
        self._one = one
        self._two = two
        self._three = three

    def getclass1_accessors(self):
        return (self._one, self._two, self._three)

    def Constructor():
      exampleClass = Class1(1, 2, 3)

      exampleClass.staticMtd_class1(exampleClass._one)

      exampleClass.setclass1_mutators(exampleClass._one, exampleClass._two, exampleClass._three)

      exampleClass.getclass1_accessors(exampleClass)


class Class2:
    def __init__(self, four, five, six):
        self._four = four
        self._five = five
        self._six = six
      
    @staticmethod
    def staticMtd_class2():
      return 0

    def setclass2_mutators(self, four, five, six):
        self._four = four
        self._five = five
        self._six = six

    def getclass2_accessors(self):
        return (self._four, self._five, self._six)

    def Constructor():
      exampleClass = Class2(1, 2, 3)

      exampleClass.staticMtd_class1(exampleClass._one)

      exampleClass.setclass1_mutators(exampleClass._one, exampleClass._two, exampleClass._three)

      exampleClass.getclass1_accessors(exampleClass)

class Class3:
    def __init__(self, seven, eight, nine):
        self._seven = seven
        self._eight = eight
        self._nine = nine

    @staticmethod
    def staticMtd_class3():
      return 0

    def setclass3_mutators(self, seven, eight, nine):
        self._seven = seven
        self._eight = eight
        self._nine = nine

    def getclass3_accessors(self):
        return (self._seven, self._eight, self._nine)

    def Constructor():
      exampleClass = Class3(1, 2, 3)

      exampleClass.staticMtd_class1(exampleClass._one)

      exampleClass.setclass1_mutators(exampleClass._one, exampleClass._two, exampleClass._three)

      exampleClass.getclass1_accessors(exampleClass)
