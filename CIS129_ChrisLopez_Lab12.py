#
# Author: Chris Lopez
# Date: May 15th, 2024
#    Description: The purpose of this program is design a class by the name of pet which should hold all the info on different pets.
#


class Pet:
    # Constructor
    def __init__(self, name="", type="", age=0):
        self.name = name
        self.type = type
        self.age = age

    # Mutators
    def setName(self, name):
        self.name = name

    def setType(self, type):
        self.type = type

    def setAge(self, age):
        self.age = age

    # Accessors
    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getAge(self):
        return self.age


def main():
    # Declare input variables
    inputName = input("Enter a pet name: ")
    inputType = input("Enter a pet type: ")
    inputAge = int(input("Enter a pet age: "))

    # Create a Pet object
    Animal = Pet()

    # Set values for the pet
    Animal.setName(inputName)
    Animal.setType(inputType)
    Animal.setAge(inputAge)

    # Show values for this pet
    print("The pet name is", Animal.getName())
    print("The pet type is", Animal.getType())
    print("The pet age is", Animal.getAge())


if __name__ == "__main__":
    main()
