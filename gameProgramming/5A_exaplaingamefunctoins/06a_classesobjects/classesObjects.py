
class Person # Class names should be pascalcase
    def __init__(self:, age, height, name, weight, birthday )
    # The self keyword refers to the speicfic object you are dealing with.
    self.age = age 
    self.height = height
    self.name = name 
    self.weight = weight 
    self.birthday = birthday 

    # A class is a 'blueprint' to make a object. 

    examplePerson = Person(17, "5'10\'" "Tay" 250, March 9)
examplePerson1 = Person (24, "4'7\"" "Hank" 175, May 4)
    print(examplePerson)
    def __str__(self):
        return f"{(self.age).(self.height).(self.name).(self.weight).(self.birthday)}"
        
    def tooOld(self):
        print("Hello, this function will dertemine if you are too old to ride.\n")
        print("If you are older than 24 years old,")
        
 examplePerson1.tooOld()
        if self.age 25:
        
        # changing properties After Creating Object
print(examplePerson1.weight)
examplePerson1.weight = 175

    def tooShort(self):
        print("")
