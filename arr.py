##PRACTICE
##Print only duplicate value in array program (same program write diff.-diff. method and diff. logic)
## Method-1
# arr = [1 ,1, 5, 5, 3, 4, 8, 7, 9, 9, 0, 6]
# duplicate = set()
# for i in arr:
#     if arr.count(i) > 1:
#         duplicate.add(i)

# print("This Duplicate value :", duplicate)


##Method-2
# numbers = [10, 20, 30, 20, 40, 10, 50, 30, 60] 
# seen = [] 
# duplicates = [] 
# for num in numbers: 
#     if num in seen: 
#         if num not in duplicates: 
#             duplicates.append(num) 
#     else: 
#         seen.append(num) 
    
# print("Duplicate elements:", duplicates)



# arr = [10, 20, 30, 40, 20, 50, 20]

# print(arr.count(20))
# print(len(arr))

# print(max(arr))
# print(min(arr))

# print(sum(arr))


##Print average using sum() and len()
# arr = [10, 20, 30, 40, 50, 60, 70]

# sum_arr = sum(arr)
# len_arr = len(arr)
# avg = sum_arr / len_arr

# print(avg)


##Check 20 in arr
# arr = [5, 10, 15, 20, 25]

# if 20 in arr:
#     print(True)
# else:
#     print(False)


##Find index
# arr = [10, 20, 30, 40, 50]

# print(arr.index(30))


# arr = [10, 20, 30, 40, 50, 20, 10]

# duplicate = []

# for i in arr:
#     if arr.count(i) > 1:
#         duplicate.append(i)
        
# print("Duplicate value :", duplicate)

##Sort array
# arr = [5, 2, 8, 1, 9, 3]

# arr.sort()
# print(arr)
# arr.sort(reverse=True)
# print("Reverse array :", arr)


# arr = [10, 20, 40, 50, 60]
# arr.insert(2, 30)
# arr.append(70)
# print(arr)
# arr.remove(30)
# print(arr)
# arr.pop(5)
# print(arr)


# arr1 = [1, 2, 3]
# arr2 = [4, 5, 6]

# arr = arr1.extend(arr2)
# print(arr1)


# def is_even(n):
#     return n % 2 == 0

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# a = filter(is_even, arr)
# print(list(a))
# print(any(arr)) #check even in arr (True/False)
# print(all(arr)) #check number is positive (True/False)


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for index, value in enumerate(arr): #print index and value both are print
#     print(index, value)
    
    
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2]

# arr.reverse()
# print(arr)
# print(set(arr))
# print(arr)


# arr = [1, 2, 4, 8, 9, 10]

# print("Second largest :", arr[-2])