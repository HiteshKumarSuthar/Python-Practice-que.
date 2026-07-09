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
name = ("Hitesh", "Kumar", "Hitesh")  #object

new_name = ("Suthar",)  #object

all_name = name + new_name  #object

print(all_name)

#check condition
if "Hitesh" in name:
    print(True)
else:
    print(False)
    
    
#count
print(name.count("Hitesh"))

#as a variable use 
(hitesh, kumar, hitesh) = name
print(hitesh)

#type
print(type(name))


#Nesting tuple
x = ("Hitesh", (11), "Kumar", ("suthar"))

print(x)
