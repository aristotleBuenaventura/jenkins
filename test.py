class Person:
    def __init__(self,name,age):
        self.name = name
        self.age=age

    def printDetails(self):
        print(f"Hi my name is {self.name} and I'm {self.age} years old")


person1 = Person("Aristotle",25)
person1.printDetails()
