class NameOfClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def method(self):
        print(self.param1)


########################################################################################################################
class Dog:

    # Class Obj Attribute, same for all instances
    species = 'Mammal'

    def __init__(self, mybreed, name, spots):
        """
        Creates Dog objects to document class creation
        :param mybreed:
        :param name:
        :param spots:
        """
        # Attributes
        self.breed = mybreed
        self.name = name
        self.spots = spots

    def bark(self, number):
        """

        :param number:
        :return:
        """
        print("WOOF! My name is {} and the number is: {}".format(self.name, number))


my_dog = Dog("Spaniel", "Zoey", True)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print()
print(my_dog.species)
print()
my_dog.bark(13)
print()
print()
print()
print()


########################################################################################################################
class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        """
        Creates a circle with default radius of 3
        :param radius:
        """
        self.radius = radius
        self.area = radius * radius * Circle.pi

    def get_circumference(self):
        """
        Finds the circumference
        :return:
        """
        return self.radius * Circle.pi * 2


mycircle= Circle()
print(mycircle.pi)
print(mycircle.radius)
print(mycircle.get_circumference())

print()
print()
print()
print()


########################################################################################################################
class Animal:
    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cat Created")

    def whoAmI(self):
        print("I am a cat")

    def meow(self):
        print("Meow")


mycat = Cat()
myanimal = Animal()
mycat.eat()
myanimal.eat()
mycat.whoAmI()
myanimal.whoAmI()
mycat.meow()
# myanimal.meow

print()
print()
print()
print()


########################################################################################################################
class Wolf:
    def __init__(self, name):
        """

        :param name:
        """
        self.name = name

    def roar(self):
        """

        :return:
        """
        return self.name + " Roars"


class Lion:
    def __init__(self, name):
        """

        :param name:
        """
        self.name = name

    def roar(self):
        """

        :return:
        """
        return self.name + " Purrs"


niko = Wolf("niko")
felix = Lion("felix")

print(niko.roar())
print(felix.roar())

print()

for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.roar()))


# TAKES ADVANTAGE OF BOTH WOLF AND LOIN HAVING METHODS CALLED ROAR
# TO BE ABLE TO CALL LIKE THIS IS CALLED POLYMORPHISM
def pet_roar(pet):
    print(pet.roar())


print()

pet_roar(niko)
pet_roar(felix)


# An example of an ABSTRACT METHOD:
# Parent method that will never be called as an object, but rather a template for other classes
class Creature:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


# Example of abstract class that could be used to open different types of files
class Open:
    def open(self):
        raise NotImplementedError("Subclass must implement this abstract method")


print()
print()
print()
print()


########################################################################################################################
class Book:
    def __init__(self, title, author, pages):
        """

        :param title:
        :param author:
        :param pages:
        """
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")


b = Book("Python Rocks", "Mike", 200)

print(b)
print(len(b))
del b