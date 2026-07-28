# Scope = Variable
# LEGB - 1.Local Scope, 2. Enclosing Scope, 3. Global Scope, 4. Built-In Scope

# 1. Local Scope - Accessible only in the method. Cannot access outside.
# name = "Chirag"
# def local_scope():
#     name = "Hitesh"
#     # print(name)
#     second_name = "Suresh"
#     name = second_name
#     # print(name)
# local_scope()
# print(name) # Cannot access outside the method.

# -------------------------------------------------------------------------

# 3. Global Scope
# Accessible anywhere in the code.
# number = 12345
# def global_scope():
#     number_1 = 54321
#     print(number_1 + number)
# global_scope()
# print(number)

# -------------------------------------------------------------------------

# 4. Built-in Scope
# numbers = [1,2,3,4,5]
# name = "Hitesh Suthar"
# x = 12345
# print(numbers)

# ------------------------------------------------------------------------

# 2. Enclosing Scope
# y = 300 # Globale Scope
# def outside():
#     x = 500
    
#     def inner():
#         print("Printing from the inner() method: ",x) # Enclosing Scope (Variable), Output: 500
#         # print("Inner is printing nothing!")
       
#     inner()
    
# outside()
# print(y) # Output: 300



# Question 1: Highest Even Number

# Ek function highest_even(numbers) banao jo list ko parameter ke roop me le.

# Rules:

# Agar list me even numbers hain, to sabse bada even number return karo.
# Agar koi even number nahi hai, to "No Even Number" return karo.
# Built-in max() function ka use mat karo.

# Example:

# highest_even([5, 2, 9, 12, 7, 18])
# # Output: 18

# highest_even([1, 3, 5])
# # Output: No Even Number


def highest_even(lst):
    lst = [5, 2, 9, 12, 7, 18]
    
    highest_even_num = None
    for i in lst:
        if i % 2 == 0:
            if highest_even_num is None or i > highest_even_num:
                highest_even_num = i
    return highest_even_num


lst = [5, 2, 9, 12, 7, 18]
result = highest_even(lst)
print("Highest Even Number :", result)

