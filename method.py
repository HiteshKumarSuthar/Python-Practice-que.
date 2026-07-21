# def display(text, times):
    
#     if text == "I love you" or text == "Sorry":
#         for i in range(1, times+1):
#             print(i,".",text)
            
#     else:
#         print(f"{text} is not accepted!")
        

# display(input("Enter your message: "), int(input("How many times? :  ")))


#Q-1
# def greet():
#     print("Welcome to Python Programming")

# greet()
# greet()
# greet()
# greet()
# greet()

#Q-2
# def square():
#     print(13 ** 2)
    
# square()

#Q-3
# Create two functions even() and odd(). even() should print all even numbers from *1 to 20, and odd() should print all odd numbers from **1 to 20*.


while True:
    
    def even():
        for i in range(1, 21):
            if i % 2 == 0:
                print(i)


    def odd():
        for i in range(1, 21):
            if i % 2 != 0:
                print(i)
                
    
    print("1. Even number")
    print("2. Odd number")
    print("3. Exit")
    
    choice = int(input("Enter your Choice : "))
    
    if choice == 1:
        even()
    elif choice == 2:
        odd()
    elif choice == 3:
        print("Your are left this program!")
        break
    else:
        print("Invalid choice....")

