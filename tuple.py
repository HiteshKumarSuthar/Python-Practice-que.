##----TUPLE----

##-Que.-
# item = ("suresh", "hitesh", "chirag", "ramesh", "kishor", "aryan", "ramesh", "kishan", "abhinav", "harsh")

# print(item)

# for i in item:
#     if "a" in i:
#         print(i)


# for i in item:z
#     if i[1] == "a":
#         print(i)

#-Q1-
# tup = (1, 2, 3)

# tup[1] = 2

# print(tup)

#-Q2-
# name = ("Hitesh", "Kumar", "Hitesh")  #object

# new_name = ("Suthar",)  #object

# all_name = name + new_name  #object

# print(all_name)

# #check condition
# if "Hitesh" in name:
#     print(True)
# else:
#     print(False)
    
    
# #count
# print(name.count("Hitesh"))

# #as a variable use 
# (hitesh, kumar, hitesh) = name
# print(hitesh)

# #type
# print(type(name))


# #Nesting tuple
# x = ("Hitesh", (11), "Kumar", ("suthar"))

# print(x)



##-Que-

# value = (1, 2, 3, 4, 1)


# print(value[0])
# print(value[3])
# print(value[-1])
# print("Length is :", len(value))

# for tup in value:
#     print(tup)

# i = 0
# while i < (len(value)):
#     print(value[i])
#     i += 1

# print(sum(value))

# print(max(value))
# print(min(value))

# print(value.count(1))

# print(value.index(4))


# print(value * 3)

# print(value[2 : 4])
# print(value[0 : 3])


#convert tuple to list
# convert = list(value)

# print(convert)


##Clean duplicate
# a = [1, 1, 1, 2, 2, 2, 3, 3, 3]

# b = []

# for i in a:
#     if i not in b:
#         b.append(i)
    

# print(a)
# print(b)   


number = int(input("Enter the number : "))

num = (1, 2, 3, 4, 1, 4, 2, 1, 5)

count = 0

for i in num:
    if number == i:
        count += 1

print(count)

