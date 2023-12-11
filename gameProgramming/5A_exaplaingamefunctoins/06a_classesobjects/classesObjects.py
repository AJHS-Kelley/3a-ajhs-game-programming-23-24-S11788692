
class Person # Class names should be pascalcase
    def __init__(self, age, height, name, weight, birthday )
    # The self keyword refers to the speicfic object you are dealing with.
    self.age = age 
    self.height = height
    self.name = name 
    self.weight = weight 
    self.birthday = birthday 

    # A class is a 'blueprint' to make a object. 

    examplePerson = Person(17, "5'10\'" "Tay" 250, March 9)
examplePerson1 = Person (24, "4'7")
    print(examplePerson)
