##----DICTIONARIES----

##Accessing Dictionary Items
# d = {"name": "Hitesh", "age": 21}

# print(d["name"])     # Access using key
# print(d.get("age"))  # Access using get()

# d = {"name": "Sam"}


##Adding and Updating Dictionary Items
# d["age"] = 21        # Adding a new key-value pair
# d["name"] = "Alex"   # Updating an existing value
# print(d)




# student_details = {
#     "name" : "Hitesh",
#     "age" : 19,
#     "Branch" : "CSE",
# }
# print(student_details)
# print(student_details.get("name"))


# student_details["name"] = "Suresh"
# print(student_details)


# #Using for loop
# for i in student_details:
#     print(i, ":", student_details[i])


# for key, value in student_details.items():
#     print(key, value)
    
    
# if "name" in student_details:
#     print("True")
    
    
# print(len(student_details))


# student_details["year"] = "second"
# print(student_details)


# print(student_details.pop("name"))
# print(student_details)


# print(student_details.popitem())
# print(student_details)



# student_details = {
    
#     "Hitesh" : {
#         "name" : "Hitesh",
#         "age" : 19,
#         "Branch" : "CSE",
#     },
#     "Suresh" : {
#         "name" : "Suresh",
#         "age" : 20,
#         "Branch" : "BCA",
#     },
#     "Chirag" : {
#         "name" : "Chirag",
#         "age" : 21,
#         "Branch" : "BCA",
#     },
# }
# print(student_details)
# print(student_details["Chirag"])



# squared_num = {x : x**2 for x in range(11)}
# print(squared_num)


#Diff. keys set and value set
# keys = ["name", "branch", "year"]
# # print(keys)
# default_value = "hitesh"
# # print(keys, default_value)

# new_dict = dict.fromkeys(keys, default_value)
# print(new_dict)

# new_dict = dict.fromkeys(keys, keys)
# print(new_dict)



##--SAMPLE DATA--
# product = {
#     "Mobile": {
#         "M1": {
#         "Brand": "Apple",
#         "Model": "17 Pro Max",
#         "Price": 189000,
#         },
        
#         "M2": {
#         "Brand": " Samsung",
#         "Model": "S26 Ultra",
#         "Price": 149000,
#         },
        
#         "M3": {
#         "Brand": "Vivo",
#         "Model": "X300 Ultra",
#         "Price": 159000,
#         },
#     },
    
#     "Laptop": {
#         "L1": {
#         "Brand": "Apple",
#         "Model": "MacBook Pro M5 Max",
#         "Price": 429900,
#         },
        
#         "L2": {
#         "Brand": "Asus",
#         "Model": "Vivobook 14 Go",
#         "Price": 45000,
#         },
        
#         "L3": {
#         "Brand": "Lenovo",
#         "Model": "LOQ",
#         "Price": 90000,
#         },
#     },
# }

# print(product["Laptop"]["L3"])


# # print(product.get())

# ##To retrieve data for a specific ID

# for key, value in product["Mobile"]["M3"].items():
#     print(key, ":", value)
# ##output    
# ## Brand : Vivo
# ## Model : X300 Ultra
# ## Price : 159000


# m1_data = product["Mobile"]["M1"]
# print(m1_data)
# ##output
# ## {'Brand': 'Apple', 'Model': '17 Pro Max', 'Price': 189000}


##Nested Dictionary
d = {
    "student" : {
        "name" : "Hitesh Kumar Suthar",
        "Class" : 12,
        "age" : 18,
    }
}

print(d["student"]["name"])
