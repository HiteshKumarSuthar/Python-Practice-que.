##Q-1

# class Student:
    
#     def __init__(self, name):
#         self.my_name = name
        
#     def display(self):
#         print("Name :", self.my_name)

        
# n = Student("Kishor")

# n.display()


##Q-2

class car:
    def __init__(self, brand, model):
        self.car_brand = brand
        self.car_model = model

    def display(self):
        print("Brand :", self.car_brand)
        print("Model :", self.car_model)

cars = car("Hyundai", "i20")
cars.display()