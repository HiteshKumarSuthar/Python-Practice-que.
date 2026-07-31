##===Exception Handling===
## Syntax Error → Code is written incorrectly, so Python can't start it.
## Runtime Error (Exception) → Code starts running but crashes while executing.
## Logical Error → Code runs successfully, but gives the wrong answer.

## ValueError
# try:
#     num = int(input("Enter a number: "))
#     print(num)
    
# except ValueError:
#     print("Please enter integer value only!")
    
# finally:
#     print("Program executed successfully!!!")



## ZeroDivisionError and ValueError
# try:
#     num1 = int(input("Enter number1: "))
#     num2 = int(input("Enter number2: "))

#     print(num1 / num2)
    
# except ValueError:
#     print("Please enter integers only...")
    
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
    
    
# finally:
#     print("Bhai kya dekh raha hai program execute ho gaya...")
    


# with open("abc.py", "r") as file:
#     content = file.read()
#     print(content)



##===File write and read using exception handiling===
## FileNotFoundError
# try:
#     with open("hitesh.txt", "w") as file:
#         file.write("Hitesh Kumar suthar")
#     with open("hitesh.txt", "r") as file:
#         content = file.read()
#         print(content)
    
# except FileNotFoundError:
#     print("File does not exist in your folder")

# finally:
#     print("Succesfully run")
    
    
# try:
#     with open("hitesh.txt", "w+") as file:
#         file.write("Hitesh Kumar suthar")
#         file.seek(0)
#         print(file.read())
    
# except FileNotFoundError:
#     print("File does not exist in your folder")

# finally:
#     print("Succesfully run")
    

## SyntaxError
# try:
#     if 5 > 2
#         print("Hello")

# except SyntaxError:
#     print("SyntaxError")


## Runtime Error
# try:
#     a = 10
#     b = 0
#     print(a / b)

# except RuntimeError:
#     print("ZeroDivisionError: division by zero") 
        

## NameError
# try:
#     print(x)

# except NameError:
#     print("NameError: name 'x' is not defined")


## IndexError
# try:
#     a = [10, 20, 30]
#     print(a[6])

# except IndexError:
#     print("IndexError: list index out of range")


## TypeError
# try:
#     a = ("11" + 5)
#     print(a)
# except TypeError:
#     print("TypeError")
    

## KeyError
# try:
#     student = {"name" : "Python"}
#     print(student["age"])
# except KeyError:
#     print("KeyError")


## AttributeError
# try:
#     a = 10
#     a.append(5)
#     print(a)
# except AttributeError:
#     print("AttributeError")
    

## ModuleNotFoundError
# try:
#     import mymoodule

# except ModuleNotFoundError:
#     print("ModuleNotFoundError")


## ImportError
# try:
#     from math import square

# except ImportError:
#     print("ImportError")


## OverflowError
# try:
#     import math
#     print(math.exp(1000))
# except OverflowError:
#     print("OverflowError")


## MemoryError
# try:
#     a = [1] * (10**20)
    
# except MemoryError:
#     print("MemoryError")


## RecursionError
# try:
#     def fun():
#         fun()
        
#     fun()
    
# except RecursionError:
#     print("RecursionError")


## KeyboardInterrupt
# try:
#     while True:
#         pass

# except KeyboardInterrupt:
#     print("KeyboardInterrupt")


## AssertionError
# try:
#     x = 5
#     assert x > 10
    
# except AssertionError:
#     print("AssertionError")


## StopIteration
# try:
#     nums = iter([1])

#     print(next(nums))
#     print(next(nums))
    
# except StopIteration:
#     print("StopIteration")
    
    
