#Q-1

# class Student:
    
#     def __init__(self, name):
#         self.my_name = name
        
#     def display(self):
#         print("Name :", self.my_name)

        
# n = Student("Kishor")

# n.display()


#Q-2

# class car:
#     def __init__(self, brand, model):
#         self.car_brand = brand
#         self.car_model = model

#     def display(self):
#         print("Brand :", self.car_brand)
#         print("Model :", self.car_model)


# cars = car("Hyundai", "i20")
# cars.display()


#Q-3

# class faculty:
#     def __init__(self, name, course):
#         self.Name = name
#         self.Course = course

#     def display(self):
#         print("Name :", self.Name)
#         print("Course :", self.Course)
        
# fac = faculty("Hitesh", "Python")
# fac.display()


# #Q-4
# class Students:
#     def __init__(self, name, address):
#         self.Name = name
#         self.Address = address

#     def display(self):
#         print(self.Name, "-", self.Address)
        
# students = []
# students.append(Students("NAME", "ADDRESS"))
# students.append(Students("Hitesh", "Jaipur"))
# students.append(Students("Suresh", "Delhi"))
# students.append(Students("Chirag", "Noida"))
# students.append(Students("Rohan", "Pune"))

# for student in students:
#     student.display()


##Q-5
# class University:
#     name = input("Please Enter your name : ")
#     age = int(input("Enter your age : "))
    
#     def addmission(name, age):
#         print(name)
#         print(age)
        
#     def display():
#         print("Your Addmission is Successfully!!!")


# add = University()
# University.display()


## Inheritance - Single Inheritance
## Base class (Parent class) = 1
## Child class (Derived Class) = 1

# class Animal: # Parent Class
#     def sounds(self):
#         print("Animal makes sound.")
        
    
# class Dog(Animal): # Derived Class
#     def sounds(self):
#         print("Dog barks.")
#     # pass


# d = Dog() # d is object
# d.sounds() # Output: Animal makes sound.


##Q-6
# class Animal():
#     def display(self):
#         print("Bull Dog")
    
# class Dog(Animal):
#     def bark(self):
#         print("Woof! Woof!")
        

# d = Dog()
# d.display()
# d.bark()


##Q-7
# class Person():
#     def show_name(self):
#         print("Name - Suresh")
        
# class Student(Person):
#     def show_details(self):
#         print("Roll no. :", 1234)
        

# s = Student()
# s.show_name()
# s.show_details()


##Q-8
# class vehicle():
#     def vehicle_brand(self):
#         print("Brand - Hyundai")
#         print("Brand - Hyundai")
#         print("Brand - Hyundai")
#         print("Brand - Hyundai")
        
# class vehicle_model(vehicle):
#     def model(self):
#         print("Model - i20")
#         print("Model - i10")
#         print("Model - creata")
#         print("Model - venue")
        
# v = vehicle_model()
# v.vehicle_brand()
# v.model()


##Q-9
# class account():
#     def __init__(self, acc_number, balance):
#         self.balance = balance
#         self.acc_number = acc_number
        
# class saving_acc(account):
#     def deposit(self, amount):
#         self.balance += amount
        
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient balance")

#     def display(self):
#         print("Account Number : ", self.acc_number)
#         print("Balance : ", self.balance)
        
# acc = saving_acc(1234, 5000)
# acc.deposit(2000)
# acc.display()
# acc.withdraw(1000)
# acc.display()

    
