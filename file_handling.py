##===File Handling===
## File Read & Write and print vowels and count a vowels in this file.

# with open("movies.txt", "w+") as file:
#     file.write("Learning Python is enjoyable because it helps solve real problems through simple code. Every practice session improves logical thinking, debugging skills, and confidence. Reading files, writing data, handling exceptions, and creating projects build practical experience. Consistent effort each day leads to stronger programming knowledge and better career opportunities.")
#     file.seek(0)
#     content = file.read()

# content_words = content.split()

# # print(content_words)

# vowels = "aeiouAEIOU"
# count = 0
# for each in content_words:
#    for word in each.split():
#        for ch in word:
#            if ch in vowels:
#                print(each)
#                count += 1 
#                break

# print("Total vowels is :", count)


## read file
# # file = open("movies.txt", "r")
# # content = file.read()

# # print(content)

# # file.close()

# with open("movies.txt", "r") as file:
   
#    content_lines = file.readlines()
#    print(content_lines)


# filtered_content_lines = []

# for each in content_lines:
#    new_each = each.replace("\n", "")
#    filtered_content_lines.append(new_each)

# print(filtered_content_lines)


##  Write+ride
# cars = ["Alto800", "\nWagonR", "\nRolls Roys"]

# with open("cars.txt", "w+") as file:
#     file.writelines(cars)
#     file.seek(0)
#     content = file.read()

# print(content)



## Input from user and write & read content in file.

con = list(map(str, input("Enter content : ").split(",")))

with open("movies.txt", "w+") as file:
    file.writelines(con)
    file.seek(0)
    content = file.read()
    
print("Content has been stored successfully...")



print("1. Write content to the file [YES]")
print("2. Exit without writing [NO]")
    
choice = int(input("Enter your choice : "))

if choice == 1:
    print(content)
    print("Data written to file successfully. Data read from file successfully.")
elif choice == 2:
    print("Nothing to read and write.")
else:
    print("Invalid choice")
    
