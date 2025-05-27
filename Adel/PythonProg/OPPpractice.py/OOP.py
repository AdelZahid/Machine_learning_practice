# class Person:
#     college_name="Titumir College"
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

# #static metnod whic a decorator whic is for class level

#     @staticmethod
#     def hello():
#         print("Hello from Person class")


#     def get_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Address: {self.address}")






# print(Person.college_name) #Class atribuite

# #object attribute
# a=Person("Adel",22,"Rampura")
# b=Person("Rassle",25,"Mohanogor")
# #attribuite can be changed from outside
# b.name="Alamin"


# a.hello()

# a.get_info()
# b.get_info()







class Car:
    def __init__(self, make, model, year, engincc, fuleconsumption, price):
        self.make = make
        self.model = model
        self.year = year
        self.engincc = engincc
        self.fuleconsumption = fuleconsumption
        self.price = price
        # Calculate the point for the car
        self.__point = (self.engincc % 100) + (self.fuleconsumption % 10) + (self.price % 10000) + (self.year % 100)

    def get_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Engine cc: {self.engincc}")
        print(f"Fuel consumption: {self.fuleconsumption}")
        print(f"Price: {self.price}")
        print("\n")

    def get_point(self):
        return self.__point


def best_car(cars):
    best_car = cars[0]
    for car in cars:
        if car.get_point() > best_car.get_point():
            best_car = car
    best_car.get_info()


# Function to create and display multiple cars
def create_and_display_cars():
    num = int(input("The number of cars: "))
    
    # Initialize an empty list to store Car objects
    cars = []
    
    for i in range(num):
        make = input("Enter the name: ")
        model = input("Enter the model: ")
        year = int(input("Enter the year: "))
        engincc = float(input("Enter the engine cc: "))
        fule_consumption = float(input("Enter the fuel consumption: "))
        price = int(input("Enter the price: "))
        # Create a new Car object and append it to the list
        car = Car(make, model, year, engincc, fule_consumption, price)
        cars.append(car)
    
    # Display information for each car in the list
    for car in cars:
        car.get_info()
    
    print("The best car is:")
    print("\n")
    
    best_car(cars)


create_and_display_cars()

