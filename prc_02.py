#*************LOOPS-QUE.*************
# Print numbers from 1 to 10
# number = 0
# for i in range(1, 11):
#     number += 1
#     print(number)


# Print reverse counting from 10 to 1.
# for i in range(10, 0, -1):
#     print(i)


# Print all even numbers from 1 to 100.
# for i in range(1, 101):
#     if i % 2 == 0:
#         print("EVEN NUMBER :", i)
     
        
#. Print all odd numbers from 1 to 100.
# for num in range(1, 101):
#     if num % 2 != 0:
#         print("ODD NUMBER :", num)


#Find the sum of numbers from 1 to N.
# n = int(input("Enter the num : "))
# total = 0


# for i in range(1, n + 1):
#     total += i
# print("SUM", total)


#Print the multiplication table of a given number.
# table = int(input("ENTER THE NUMBER : "))

# for i in range(1, 11):
#     print(table * i)


#Print the squares of numbers from 1 to 10.
# square = 0
# for i in range(1, 11):
#     print(i ** 2)
 
    
#Find the factorial of a given number.
# n = int(input("ENTER THE NUMBER :"))

# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
#     print("Factorial is :", factorial)

# print(factorial)

#FACTORIAL METHOD KESE NIKALTE HAI FACT.
# 5! = 5 × 4 × 3 × 2 × 1 = 20

#    = 20 × 3 × 2 × 1 = 60

#    = 60 × 2 × 1 = 120

#    = 120 × 1 = 120 (Final this factorial is 5! = 120)

#    = 120


#Print the first N terms of the Fibonacci series.


#Print all numbers from 1 to 100 that are divisible by 3.
# number = 0
# for i in range(1, 101):
#     if i % 3 == 0:
#         print("THIS NUMBER IS DIVISIBLE BY 3 :", i)


#Print each character of a string on a new line.
# c = "Hitesh"

# for i in c:
#     ch = i
#     print(ch)


# Print all elements of a list using a loop.
# element = ["Hitesh", "Kumar", "Suthar", 11]

# for i in element:
#     print(i, end=", ")
    
#Generate the following star pattern:
# star = '*'

# for i in range(1, 6):
#     print(star * i)
    

#Generate the following reverse star pattern:
# star = '*'

# for i in range(5, 0, -1):
#     print(star * i)
    

#Print numbers from 1 to 50, but break the loop as soon as it reaches 25.
# number = 0

# for i in range(1, 50):
#     if i == 25:
#         break
#     print(i)



#*************IF-ELSE-QUE.*************
#Check whether a number is positive, negative, or zero.
#Use Nested 
# number = int(input("Enter the number : "))

# if number > 0:
#     print("Positive Number")
# else:
#     if number < 0:
#         print("Neagative Number")
#     else:
#         if number == 0:
#             print("This number is zero")


#Check whether a number is even or odd.
#use Nested
# Check_number = int(input("Enter the number : "))

# if Check_number % 2 == 0:
#     print("This Number is Even number")
# else:
#     if Check_number % 2 != 0:
#         print("This Number is Odd Number")
        

#Find and print the larger of two numbers.

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))

# if a >= b or b > a:
#     print(f"{a} is larger")
#     if b >= a or b > c:
#         print(f"{b} is larger")
#     else:
#         if c >= b or a > c:
#             print(f"{c} is larger")
#         else:
#             if c > b:
#                 print(f"{c} is larger")
            
            
#5. Check whether a student has passed or failed (Passing Marks = 33).

student = int(input("Enter the number : "))

if student >= 90:
    print("A+ GRADE AND PASS")
else:
    if student >= 80:
        print("A GRADE AND PASS")
    else:
        if student >= 75:
            print("GRADE C AND PASS")
        else:
            if student >= 60:
                print("GRADE D AND PASS")
            else:
                if student == 33:
                    print("THIS MARKS ONLY PASSING MARKS AND YOU'RE GRACE PASS")
                else:
                    if student < 33:
                        print("FAIL!! BETTER LUCK NEXT TIME")


