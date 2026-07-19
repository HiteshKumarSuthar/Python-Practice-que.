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
# d = {
#     "student" : {
#         "name" : "Hitesh Kumar Suthar",
#         "Class" : 12,
#         "age" : 18,
#     }
# }

# print(d["student"]["name"])



##====Que.====
# students = {}

# number_of_students = int(input("How many students? : "))

# for i in range(1, number_of_students+1):
#     name = input("Enter your name: ")
    
#     while True:
        
#         age = int(input("Enter your age: "))
        
#         if age > 0 and age <= 100:
#              break
#         else:
#             print("Invalid age")
            
            
#     course = input("Your course: ")
#     city = input("Which is your city? : ")

#     ##int -> str
#     format_1 = "Student"
#     number = i
#     student_id = format_1 + str(number)

#     students[student_id] = {
#         "name": name,
#         "age": age,
#         "course": course,
#         "city": city
#     }
    
# find_id = input("Enter the student id (eg. Student1, Student2....) : ")


# for key,value in students.items():
#     if find_id == key:
#         print(value)
#         break
#     else:
#         print("No student found!")
        
        

##====Question 3: Simple Inventory Management System====

# Create a dictionary to store product details.

# Each product should have:

# Product ID
# Product Name
# Price
# Quantity

# Use a menu-driven program to perform the following operations:

# Add a new product.-
# Search a product using Product ID.
# Display all products.
# Exit the program.

# Conditions:

# Product ID must be unique.
# Price and Quantity cannot be negative.
# Store product details using nested dictionaries.


# Add = input("Enter a New Product Add : ")
# Search = input("Search a Product Using ID : ")
# Exit = input("Exit this Menu : ")




##====PRODUCT INVENTORY PROGRAM====
# products = {}

# while True:
#     print("\n**** Product Inventory Management ****")
#     print("1. Add Product")
#     print("2. Delete Product")
#     print("3. Search Product")
#     print("4. Display Products")
#     print("5. Exit")
    
#     choice = int(input("Enter your choice between (1-4) : "))
    
#     if choice == 1:
#         while True:
#             product_id = int(input("Enter Product_id (must be unique) : "))
            
#             if product_id not in products:
#                 break
#             else:
#                 print("Invalid id")
                
#         product_name = input("Enter product name : ")
#         price = int(input("Enter product price (INR) : "))
#         quantity = int(input("Enter product quantity : "))
        
#         products[product_id] = {
#             "Product Name": product_name,
#             "Price": price,
#             "Quantity": quantity
#         }
        
#         print("\nProduct added successfully!")
    
#     elif choice == 2:
#         input_product_id = int(input("Enter product id : "))
        
#         if input_product_id in products:
#             del products[input_product_id]
#             print("Product deleted...")
#         else:
#             print("Product not found!")
        
#     elif choice == 3:
#         search_product_id = int(input("Enter the product id : "))
        
#         for productid, productdetails in products.items():
#             if search_product_id == productid:
#                 print(productid, ":", productdetails)
            
            
#     elif choice == 4:
#        for productid, product_details in products.items():
#            print(productid, ":", product_details)
           
#     elif choice == 5:
#         print("Thank you for using this product inventory")
    
#     else:
#         print("Invalid choice")




##===Question===
# #Q-1
# dict = {
#     "name" : "Hitesh",
#     "age" : 20,
#     "city" : "jaipur"
# }
# print(dict)

# #Q-2
# print(dict["name"])

# #Q-3
# dict["course"] = "BTech"
# print(dict)

# #Q-4
# dic = {}

# for ch in dict:
#     if ch in dic:
#         dic[ch] += 1
#     else:
#         dic[ch] = 1
        
# print(dic)

#Q-5
