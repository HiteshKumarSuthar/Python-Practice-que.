##----LIST-QUESTION----

##Q-1
# star = "*"

# for i in range(1, 6):
#     print(star * i)
#     i += 1

#Q-2
# num = [90, 46, 748, 65, 98, 35]

# largest = max(num)
# smallest = min(num)

# print("Largest number is  : ", largest)
# print("smallest number is : ", smallest)

#Q-3
# num = [90, 46, 748, 65, 98, 35]

# num_sum = sum(num)

# print("Sum is : ", num_sum)

#Q-4
# number = [45, 334, 98, 67, 22, 11, 90, 45]

# avg = sum(number) / len(number)
# print("Average is : ", avg)

#Q-5
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# even_count = 0
# odd_count = 0


# for i in number:
#     if i % 2 == 0:
#         print(i, "Even numbers")
#         even_count += 1
#     elif i % 2 != 0:
#         print(i, "Odd number")
#         odd_count += 1
        
# print("Even count is :", even_count)
# print("Odd count is : ", odd_count)

#Q-6
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# print(number[::-1])

# #Q-7
# numbers = [34, 5, 7, 23, 65, 798, 23, 88, 44]

# numbers.sort()
# numbers.sort(reverse=True)
# print(numbers)

#Q-8
# numbers = [34, 5, 7, 23, 65, 798, 23, 88, 44]

# #without indexing
# largest = max(numbers)
# numbers.remove(largest)

# second_largest = max(numbers)
# print("Without indexing->", second_largest)

# #With indexing
# print("With indexing->", numbers[6])

#Q-9
# number = [2, 5, 3, 6, 8, 9]

# square = []

# for i in number:
#     square.append(i ** 2)
    
# print(square)

#Q-10
# number = [2, 5, 3, 6, 8, 9]
# numbers = [34, 5, 7, 23, 65, 798, 23, 88, 44]

# # number.append(numbers)
# # print(number)

# #Merge two list
# num = number + numbers
# print(num)

#Q-11
# numbers = [34, 5, 7, 23, 65, 798, 44, 88, 23, 88, 44]

# unique = list(set(numbers))
# print(unique)

#Q-12
# items = ["tv", "laptop", "desktop", "phone", "headphone"]

# for item in items:
#     print(item, end=", ")
    


#Q-13

# device = input("Find your device : ")
# items = ["tv", "laptop", "desktop", "phone", "headphone"]

# for i in items:
#     if device == i:
#         print(i)

#Q-14

# lst = []

# lst.insert(0, 2)
# lst.append(4)
# lst.insert(2, 6)

# print(lst)

# lst.reverse()
# lst.remove(2)
# print(lst)


#Q-15
# system = ["laptop", "iphone", "macbook", "ipod", "alexa"]

# items = input("Find your system : ")

# for i in system:
#     if items == i:
#         print("This system available : ", i)
        

#Q-16
# number = int(input("Enter the number "))

# for i in range(1, 20):
#     if i% number == 0:
#         print(i, "even number")
#     else:
#         print(i, "Odd number")
#         i += 1
        

##----PRACTICE-QUESTION----

# fruits = ["Mango", "Apple", "Orange", "Litchi", "Muskmalon"]

# fruits[0:1] = ["Banana"] #replace 0th index 

# fruits.pop() #last element remove

# print(fruits)

# #Using loop element check
# for i in fruits:
#     if "Apple" in i:
#         print("True")



##(X**2) square
# squared_number = [x**2 for x in range(10)]
# print(squared_number)

# ##(x**3) cube
# cube_number = [x**3 for x in range(10)]
# print(cube_number)


##copy() method
# fruits = ["Mango", "Apple", "Orange", "Litchi", "Muskmalon"]

# fruits_copy = fruits.copy()
# fruits_copy.append("lemon")

# print(fruits)
# print(fruits_copy)


##Percentage calculator
# your_marks = int(input("Enter your marks : "))

# percentage = your_marks / 500 * 100

# print(percentage)


##que
# num = [1, 3, 5, 2, 4]

# num.extend([7, 6])
# num.sort()

# print(num)


##que
number = [1, 2, 3, 4, 5, 6, 1]

# number.remove(1)
print(number)

print(number.count(1))
print(number.index(1))
print(number.clear())
number.append(1)
print(number)

