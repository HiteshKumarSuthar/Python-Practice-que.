# ##===FUNCTION (METHOD)===
# ## FUNCTION IS TWO TYPE => 1.BUILT-IN 2.USER-DEFINED

# num = [10, 54, 23, 11, 76]

# print("length is -", len(num))
# print("maximum number is -", max(num))
# print("minimum number is -", min(num))
# print("sum is -", sum(num))
# print("sorted list -", sorted(num))


# ##EX.1
# a = "10"
# b = "20"

# num = int(a) + int(b)

# print("num is -", num)



# ##USER-DEFINED-FUNCTION
# ##syntax
# def name():

#     print("hitesh")

# name()


# def hitesh(name, age):

#     print(name)
#     print(age)

# hitesh(name = input("Enter your name : "))
# hitesh(age = int(input("Enter your age : ")))


# def number(num1, num2, num3, num4):
#     sum = num1 + num2 + num3 + num4
#     avg = sum / 4
#     print("sum is :", sum)
#     print("average is :", avg)
    
# number(10, 20, 67, 50)  


# def hitesh(name, age, section, city):
#     print(name)
#     print(age)
#     print(section)
#     print(city)
    
# hitesh("Hitesh", 20, 'D', "jaipur")


# def greet(name):
#     print("My name is", name)
    
# greet("Hitesh")


##Keyword Argument
# def student(name, age):
#     print("Name is", name)
#     print("Age is", age)
    
# student(name = "hitesh", age = 19)


##Default Argument
# def greet(name = "Student"):
#     print("Hello", name)
    

# greet()
# greet("Hitesh")


# def add_num(number):
#     total = 0
#     for n in number:
#         total = total + n
#         print("Sum is", total)
        
        
# add_num(10, 23)
# add_num(10, 30, 50, 60)


# def square(num):
#     n = num * num
#     print(n)

# square(5)



##Local & Global variable
x = 100   # => Global variable

def show():
    x = 50   # => Local Variable
    print("Inside function :", x)

show()
print("Outside function :", x)
