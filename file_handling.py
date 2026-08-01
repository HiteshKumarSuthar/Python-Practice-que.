##===File Handling===
## File Read & Write and print vowels and count a vowels in this file.

with open("movies.txt", "w+") as file:
    file.write("Learning Python is enjoyable because it helps solve real problems through simple code. Every practice session improves logical thinking, debugging skills, and confidence. Reading files, writing data, handling exceptions, and creating projects build practical experience. Consistent effort each day leads to stronger programming knowledge and better career opportunities.")
    file.seek(0)
    content = file.read()

content_words = content.split()

# print(content_words)

vowels = "aeiouAEIOU"
count = 0
for each in content_words:
   for word in each.split():
       for ch in word:
           if ch in vowels:
               print(each)
               count += 1 
               break

print("Total vowels is :", count)
