# ##===METHODS(Function)===

# def display(text, times):
    
#     if text == "Welcome to python program" or text == "Exit this program":
#         for i in range(1, times+1):
#             print(i,".",text)
            
#     else:
#         print(f"{text} is not accepted!")
        

# display(input("Enter your message: "), int(input("How many times? :  ")))



# ##===Q-1===
# def greet():
#     print("Welcome to Python Programming")

# greet()
# greet()
# greet()
# greet()
# greet()



# ##===Q-2===
# def square():
#     print(13 ** 2)
    
# square()



# ##===Q-3===
# # This Menu-driven Program

# while True:
    
#     def even():
#         for i in range(1, 21):
#             if i % 2 == 0:
#                 print(i)


#     def odd():
#         for i in range(1, 21):
#             if i % 2 != 0:
#                 print(i)
                
    
#     print("1. Even number")
#     print("2. Odd number")
#     print("3. Exit")
    
#     choice = int(input("Enter your Choice : "))
    
#     if choice == 1:
#         even()
#     elif choice == 2:
#         odd()
#     elif choice == 3:
#         print("Your are left this program!")
#         break
#     else:
#         print("Invalid choice....")



# ##===Q-4===
# # Create a function calculator() that displays the following menu:

   
# #    1. Addition
# #    2. Subtraction
# #    3. Multiplication
# #    4. Division
   

# #    Then call the function.

# def calculator():
#     while True:
#         print("1. Addition")
#         print("2. Substraction")
#         print("3. Multiplication")
#         print("4. Division")
#         print("5. Exit")
        
#         cal = int(input("Enter the number and calculate numbers : "))
        
#         if cal == 1:
#             number_1 = int(input("Enter the number : "))
#             number_2 = int(input("Enter the number : "))
#             print(number_1 + number_2)
            
#         elif cal == 2:
#             number_1 = int(input("Enter the number : "))
#             number_2 = int(input("Enter the number : "))
#             print(number_1 - number_2)
            
#         elif cal == 3:
#             number_1 = int(input("Enter the number : "))
#             number_2 = int(input("Enter the number : "))
#             print(number_1 * number_2)
            
#         elif cal == 4:
#             number_1 = int(input("Enter the number : "))
#             number_2 = int(input("Enter the number : "))
#             print(number_1 / number_2)
            
#         elif cal == 5:
#             print("Exit this Program")
#             break
        
#         else:
#             print("Invalid number..Please Try Again....")


# calculator()



# ##===Q-5===
# def calculator():
#     while True:
#         print("1. Addition")
#         print("2. Substraction")
#         print("3. Multiplication")
#         print("4. Division")
#         print("5. Exit")
        
#         number_1 = float(input("Enter first number : "))
#         number_2 = float(input("Enter second number : "))
        
#         def addition(num1, num2):
#             return num1 + num2
        
#         def subtraction(num1, num2):
#             return num1 - num2
        
#         def multiplication(num1, num2):
#             return num1 * num2
            
#         def division(num1, num2):
#             if num2 == 0:
#                 return "Cannot divide by zero."
#             else:
#                 return num1 / num2
                
#         cal = int(input("Enter your choice : "))
        
#         if cal == 1:
#             result = addition(number_1, number_2)
#             print(result)
           
#         elif cal == 2:
#            result = subtraction(number_1, number_2)
#            print(result)
           
#         elif cal == 3:
#             result = multiplication(number_1, number_2)
#             print(result)
            
#         elif cal == 4:
#             result = division(number_1, number_2)
#             print(result)
            
#         elif cal == 5:
#             print("Exiting...")
#             break
#         else:
#             print("Invalid number..Please Try Again....")


# calculator()



# ##===Q-6===
# def student():
#     print("Name",":","Hitesh")

# def course():
#     print("Course",":","Python")

# def college():
#     print("College",":","Poornima University")
    
# student()
# course()
# college()



#-1-
# def table(num):
#     for i in range(1, 11):
#         print(i * num)
        
# table(int(input("Enter the number : ")))


#-2-
# def table(num):
#     i = 1
#     while i <= 10:
#         print(i * num)
#         i += 1
        
# table(int(input("Enter the number : ")))




##===Create a ATM machine in python===

def atm():
    
    balance = 1000.0
    
    while True:
        
        print("1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        n = int(input("Enter the n : "))
        
        if n == 1:
            # acc_balance = float(input("Enter the balance : "))
            # balance += acc_balance
            print("Welcome to SBI Bank ATM","\nYour Account Balance :", balance)
            
        elif n == 2:
            acc_balance = float(input("Enter the deposit balance : "))
            balance += acc_balance
            print("Dear Customer, A/c XXXXXX1234 debited for Rs", balance)
        
        elif n == 3:
            acc_balance = float(input("Enter the withdraw money : "))
            balance -= acc_balance
            print("Current Balance :", balance)

        elif n == 4:
            print("Transaction has completed...\nThank you visit again !!")
            break
        
        else:
            print("Incorrect value")
            
            
atm()
