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

##Membership check
# It checks whether an element is present in a collection or not.

# Syntax => element in collection
# Syntax => element not in collection



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


# a = {1, 2, 3}
# b = {1, 4, 5}

# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))


# s = {1, 2, 3, 4}

# print(s)
# print(type(s))

##Type Casting
# l = [1, 2, 3]

# s = set(l)
# print(s)

##Heterogeneous Element
# s = {"Hitesh", 11, 11.1, True}
# print(s)


##Frozen Sets
# number = frozenset([10, 20, 30, 40]) 

# #Membership check
# print(20 in number)
# print(50 in number)

# print(number)
# print(type(number))

# #Union
# a = frozenset([1, 2, 3])
# b = frozenset([4, 5, 6])

# print(a | b)


# ##Que.
# key = frozenset(["Python", "Java"])

# data = {
#     key: "Programming Languages"
# }

# print(data)



##----PRACTICE-QUE----
#Q-1
# num = range(1, 101)

# number = {x for x in num if x % 2 == 0}
# print(number)

#Q-2
# a = {1, 2, 3, 4, 5}
# b = {3, 4, 6, 7, 8}

# print(a - b)

#Q-3
# a = {10, 20, 30, 40}
# b = {40, 50, 60, 70}

# print(a ^ b)

#Q-4
# a = {1, 2, 3, 4, 2, 5, 6, 5}

# num = {x**2 for x in a if x % 2 == 0}

# print(num)

#Q-5
# vowel = "Hitesh Suthar"

# letter = {ch.lower() for ch in vowel if ch.lower() in "aeiou"}

# print(letter)

#Q-6
# number = {}

# num = {x for x in range(1, 100) if x % 3 == 0 and x % 5 == 0}

# number = num

# print("number :", number)

#Q-7
# a = {9, 8, 7, 6}
# b = {5, 4, 6, 2}
# c = {1, 3, 6, 7}

# print("Common number in set :", a.intersection(b, c))

#Q-8
# A = {1, 2}
# B = {3, 4, 1, 2}

# print(A.issubset(B))  #True
# print(B.issubset(A))  #False

#Q-9
# letter = "HiTesH"

# w = {ch for ch in letter if ch.isupper()}
# print(w)

#Q-10
# name = "Hitesh kumar suthar"
# string = name.split()

# word = {len(x) for x in string}
# print(word)

#hash() method
# a = {"Python", "java", "js"}

# print(hash("c"))  #return hash value

# b = {1, 2, 3}

# print(1 in b)  #return 1

#-Q-1
# a = {1, 2, 3, 4}
# b = {5, 6, 1, 7}
# c = {8, 9, 10, 1}
# d = {2, 11, 12, 1}
# e = {13, 14, 1, 15}

# print(a | b | c | d | e)
# print(a & b & c & d & e)
# print(a - b - c - d - e)


# lst = [1, 2, 3, 4, 2, 4, 3, 3, 5, 7, 6]
# print("duplicate value :", lst)
# s = set(lst)
# print("unique value :", s)
# print("length is :", len(s))

