# CLASSES

car1_make = "Toyota"
car1_model = "Camry"
car1_color = "blue"
car1_price = 10000
car1_sold = False

car1_dict = {
    "make": "Toyota",
    "model" : "Camry",
    "color" : "blue",
    "price" : 10000,
    "sold" : False
}

car2_make = "Honda"
car2_model = "Accord"
car2_color = "red"
car2_price = 8000
car2_sold = False

car2_dict = {
    "make": "Honda",
    "model" : "Accord",
    "color" : "blue",
    "price" : 10000,
    "sold" : False
}

# a class = a template to create multiple *instances* of an object

# Car class --> object for my car, object for your car, object for random car, etc.

# why do class names start with a capital letter??


class Car:
    # class attributes - variables that have the same definition across *all* instances of the class
    make = "Honda"
    sold = False

    # instantiation/initialization method
    def __init__(self, car_model, car_color, car_price):
        # instance attributes - variables whose definitions are different depending on the instance
        self.model = car_model
        self.color = car_color
        self.price = car_price

    # other methods

# new instance of class = classname(arguments)
car1 = Car("Accord", "green", 12404)
print(car1)

print(car1.price)

car2 = Car("CRV", "Purple", 22404)
print(car2)

print(car2.price)

print(car1.make)
print(car2.make)



# title, genre (only fantasy), author, pages, red sticker (price dependent)
class Book():
    genre = "Fantasy"

    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

        if (self.price <= 5):
            self.red_sticker = True
        else:
            self.red_sticker = False


class ClassName():
    # class attributes go here
    classattribute = ""

    def __init__(self, arguments):
        self.instanceattribute = arguments


class ClassName():
    # class attributes go here
    classattribute = ""

    def __init__(self):
        pass