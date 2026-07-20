def display(text, times):
    
    if text == "I love you" or text == "Sorry":
        for i in range(1, times+1):
            print(i,".",text)
            
    else:
        print(f"{text} is not accepted!")
        

display(input("Enter your message: "), int(input("How many times? :  ")))

