#STRING -> String is a collection of character.

name = "Hitesh Kumar Suthar"
n = name.replace("Hitesh","Suresh")
print(n)


#1.Concatenation
str_1 = "Hitesh"
str_2 = "Kumar"
str_3 = "Suthar"

str_4 = str_1 + " " + str_2 + " " + str_3
print(str_4)


#2.Repetition
name = "offer"
print(name * 100)

a = "Hiteshkumarsuthar"

print(a[len(a)-1]) #print(a[34-1]) = print(a[33]) = 

print(a[0 : -1]) #using indexing to print unkown string without length 

print(a[ :: -1]) #using slicing to reverse string

print(a[6 : 11]) #slicing


#4.Imp. Methods --> find(), index(), split(), join()
a = "Hitesh,kumar,suthar"

print(a.find("t")) #index return
print(a.index("t")) # index return

print(a.count("t")) #total character number count

b = a.split(",") #split
print(b)
print("/".join(b)) #join
