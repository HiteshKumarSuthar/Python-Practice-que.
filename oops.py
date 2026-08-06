##Q-1

# class Student:
    
#     def __init__(self, name):
#         self.my_name = name
        
#     def display(self):
#         print("Name :", self.my_name)

        
# n = Student("Kishor")

# n.display()


##Q-2

# class car:
#     def __init__(self, brand, model):
#         self.car_brand = brand
#         self.car_model = model

#     def display(self):
#         print("Brand :", self.car_brand)
#         print("Model :", self.car_model)


# cars = car("Hyundai", "i20")
# cars.display()


##Q-3

# class faculty:
#     def __init__(self, name, course):
#         self.Name = name
#         self.Course = course

#     def display(self):
#         print("Name :", self.Name)
#         print("Course :", self.Course)
        
# fac = faculty("Hitesh", "Python")
# fac.display()


##Q-4
class Students:
    def __init__(self, name, address):
        self.Name = name
        self.Address = address

    def display(self):
        print(self.Name, "-", self.Address)
        
students = []
students.append(Students("NAME", "ADDRESS"))
students.append(Students("Hitesh", "Jaipur"))
students.append(Students("Suresh", "Delhi"))
students.append(Students("Chirag", "Noida"))
students.append(Students("Rohan", "Pune"))

for student in students:
    student.display()
    
