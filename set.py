##----SET----
##mutable, unordered, only unique value store

# a = {"Hitesh", "Suresh", "Chirag"}

# print(a)

##Set method
# fruits = {"Apple", "Banana", "Cherry", "Date", "Elderberry"}
# print(fruits)

# fruits.update({"Fig", "Grape", "Honeydew"}) # Used if you want to add multiple items to the set.

# fruits.add("Jackfruit") # Used if you want to add a single item to the set.

# print(fruits)

# print(fruits)

# fruits.remove("Banana") # Used if you want to remove a specific item from the set.

# fruits.discard("Banana") # Used if you want to remove a specific item from the set, but won't raise an error if the item doesn't exist.

# fruits.pop() # Used to remove a random item from the set.

# print(fruits)


## Methods:
## len() = To find number of total times in set.
## clear() = To clear the set. (Empty set)


## SET METHOD
# A = {1,2,3,6}
# B = {1,2,4,5}
# C = {7,8,9,1}

# print("Union:", A.union(B, C))  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

# print("Intersection:", A.intersection(B, C))  # Output: set()

# print("Difference:", A.difference(B, C))  # Output: {3, 6}



## This is a simple Python program that demonstrates the use of list comprehensions to create a list of numbers and their squares.

# choice = int(input("Enter a number to generate a list of numbers from 1 to that number: ")) # 20

# number = [x for x in range(1, choice + 1)]

# print(number)

# print("\nSquares:")

# square = [x**2 for x in number]

# print(square)

# nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

# print("You entered:", nums)



## Question 1: Create a Set and Add an Element
##Question 2: Remove Duplicates Using a Set

# a = {1, 2, 3, 4, 5}

# a.add(6)

# print(a)


# a = [1, 1, 2, 3, 4, 5, 6, 7, 7]

# b = set(a)

# print(b)

##---METHOD()-PRC----

# a = {"Hitesh", "Kumar", "Suthar"}

# a.update({"jaipur", "delhi"})
# a.add("gurgoan")

# a.remove("Hitesh")
# a.discard("Hitesh")

# a.pop()

# print(len(a))

# a.clear()

# print(a)


a = {1, 2, 3}
b = {1, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))








##----PRACTICE-QUE----
#Q-1
# num = range(1, 101)

# number = {x for x in num if x % 2 == 0}
# print(number)


