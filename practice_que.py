#*************LOOPS-QUESTION.*************

#Print numbers from 1 to 10
number = 0
for i in range(1, 11):
    number += 1
    print(number)


#Print reverse counting from 10 to 1.
for i in range(10, 0, -1):
    print(i)


#Print all even numbers from 1 to 100.
for i in range(1, 101):
    if i % 2 == 0:
        print("EVEN NUMBER :", i)
     
        
#Print all odd numbers from 1 to 100.
for num in range(1, 101):
    if num % 2 != 0:
        print("ODD NUMBER :", num)


#Find the sum of numbers from 1 to N.
n = int(input("Enter the num : "))
total = 0


for i in range(1, n + 1):
    total += i
print("SUM", total)


#Print the multiplication table of a given number.
table = int(input("ENTER THE NUMBER : "))

for i in range(1, 11):
    print(table * i)


#Print the squares of numbers from 1 to 10.
square = 0
for i in range(1, 11):
    print(i ** 2)
 
    
#Find the factorial of a given number.
n = int(input("ENTER THE NUMBER :"))

factorial = 1
for i in range(1, n + 1):
    factorial *= i
    print("Factorial is :", factorial)

print(factorial)

#FACTORIAL METHOD KESE NIKALTE HAI FACT.
#For my understanding
# 5! = 5 × 4 × 3 × 2 × 1 = 20

#    = 20 × 3 × 2 × 1 = 60

#    = 60 × 2 × 1 = 120

#    = 120 × 1 = 120 (Final this factorial is 5! = 120)

#    = 120


#Print the first N terms of the Fibonacci series.


#Print all numbers from 1 to 100 that are divisible by 3.
number = 0
for i in range(1, 101):
    if i % 3 == 0:
        print("THIS NUMBER IS DIVISIBLE BY 3 :", i)


#Print each character of a string on a new line.
c = "Hitesh"

for i in c:
    ch = i
    print(ch)


#Print all elements of a list using a loop.
element = ["Hitesh", "Kumar", "Suthar", 11]

for i in element:
    print(i, end=", ")
    
#Generate the following star pattern:
star = '*'

for i in range(1, 6):
    print(star * i)
    

#Generate the following reverse star pattern:
star = '*'

for i in range(5, 0, -1):
    print(star * i)
    

#Print numbers from 1 to 50, but break the loop as soon as it reaches 25.
number = 0

for i in range(1, 50):
    if i == 25:
        break
    print(i)



#*************IF-ELSE-QUESTION.*************

#1.Check whether a number is positive, negative, or zero.
#Use Nested 
number = int(input("Enter the number : "))

if number > 0:
    print("Positive Number")
else:
    if number < 0:
        print("Neagative Number")
    else:
        if number == 0:
            print("This number is zero")


#2.Check whether a number is even or odd.
#use Nested
Check_number = int(input("Enter the number : "))

if Check_number % 2 == 0:
    print("This Number is Even number")
else:
    if Check_number % 2 != 0:
        print("This Number is Odd Number")
        

#3.Find and print the larger of two numbers.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b or b > a:
    print(f"{a} is larger")
    if b >= a or b > c:
        print(f"{b} is larger")
    else:
        if c >= b or a > c:
            print(f"{c} is larger")
        else:
            if c > b:
                print(f"{c} is larger")
            

#4. Find and print the largest among three numbers.


#5.Check whether a student has passed or failed (Passing Marks = 33).

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
                    

#6. Check whether a person is eligible to vote (Age ≥ 18).

age = int(input("Enter your age : "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible vote")
    
    
#7. Check whether a given year is a leap year or not.

year = int(input("Enter the year : "))

if year % 400 == 0:
    print("It is a Leap year")
else:
    if year % 100 == 0:
        print("It is Not a Leap year")
    else:
        if year % 4 == 0:
            print("It is a Leap year")

#8. Check whether a number is divisible by 5.

num = int(input("Enter the number : "))

if num % 5 == 0:
    print("Number is divisble by 5")
else:
    print("Number is not a divisble by 5")


#9.Implement a grading system based on the following rules:
#90+ → A | 75–89 → B | 60–74 → C | 33–59 → D | Below 33 → Fail

Check_grading = int(input("Enter the student marks : "))

if Check_grading >= 90:
    print("Grade - A")
elif Check_grading <= 89 and Check_grading >= 75:
    print("Grade - B")
elif Check_grading <= 74 and Check_grading >= 60:
    print("Grade - C")
elif Check_grading <= 59 and Check_grading >= 33:
    print("Grade - D")
elif Check_grading < 33:
    print("Fail")
    

#10. Check whether a character is a vowel or a consonant.

ch = input("Enter Vowels or Consonant : ")

if ch.lower() in "aeiou" :
    print("Vowel")
else:
    print("Consonant")


#11. Check whether a character is in uppercase or lowercase.

character = input("Enter the upper case or lower case character : ")

if character.islower():
    print("Lower Case")
else:
    print("Upper Case")


#12. Given three sides, check whether a triangle can be formed.

a = int(input("Enter the number and check triangular : "))
b = int(input("Enter the number and check triangular : "))
c = int(input("Enter the number and check triangular : "))

if a + b > c and a + c > b and b + c > a:
    print("Triangular can be formed")
else:
    print("Triangular cannot be formed")
    

#13.Check whether a number is divisible by both 2 and 3.

number = int(input("Enter the and check number divsible by 2 and 3 : "))

if number % 2 == 0 and number % 3 == 0:
    print("Divsible by both number")
else:
    print("It cannot be divsible by both number")
    

#14.Calculate the electricity bill using simple slab logic.

unit = int(input("Enter your electricity unit and check your bill : "))
bill = unit * 2
bill_1 = unit * 3
bill_2 = unit * 4
if unit >= 1 and unit <= 100:
    print("Your Bill is :", bill)
elif unit >= 101 and unit <= 200:
    print("Your Bill is :", bill_1)
elif unit > 200:
    print("Your Bill is :", bill_2)


#15. Build a simple calculator (+, -, *, /) using if-elif-else structures.

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))
operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    print("This Addition Number :", num_1 + num_2)
elif operator == '-':
    print("This Subtraction Number :", num_1 - num_2)
elif operator == '*':
    print("This Multiplication Number :", num_1 * num_2)
elif operator == '/':
    if num_2 != 0:
        print("This Division Number :", num_1 / num_2)
    else:    
        print("Division by zero is not possible.")
else:
    print("Invalid Operator")
