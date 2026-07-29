##===Exception Handling===
# try:
#     num = int(input("Enter a number: "))
#     print(num)
    
# except ValueError:
#     print("Please enter integer value only!")
    
# finally:
#     print("Program executed successfully!!!")

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
    

try:
    with open("hitesh.txt", "w+") as file:
        file.write("Hitesh Kumar suthar")
        file.seek(0)
        print(file.read())
    
except FileNotFoundError:
    print("File does not exist in your folder")

finally:
    print("Succesfully run")
    
