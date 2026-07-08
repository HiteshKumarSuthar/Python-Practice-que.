##----PRACRICE-QUESTION----

##-Q-1-
student = {
    "name" : "Hitesh",
    "age" : 19,
    "city" : "jaipur",
}

# print(student)

# for key, value in student.items():
#     print(key, ":", value )
    
print(student["name"])

#New kay value add
student["mobile"] = "iphone"
print(student)

#update age
student["age"] = 20
print(student)

#delete city key, value
del student["city"]
print(student)

#all key print using for loop 
for i in student:
    print(i)

#All value print
print(student.values())

#copy
print(student.copy())

#clear
print(student.clear())
