##===Program(1) ATM machine in python (Without Verification ATM machine program)===

def ATM():
    
    balance = 1000.0
    
    pin = int(input("Enter your pin : "))
    
    while True:
        
        print("1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        n = int(input("Enter the n : "))
        
        if n == 1:
            # acc_balance = float(input("Enter the balance : "))
            # balance += acc_balance
            print("Welcome to SBI Bank ATM","\nYour Account Balance :", balance)
            
        elif n == 2:
            acc_balance = float(input("Enter the deposit balance : "))
            balance += acc_balance
            print("Dear Customer, A/c XXXXXX1234 debited for Rs", balance)
        
        elif n == 3:
            acc_balance = float(input("Enter the withdraw money : "))
            balance -= acc_balance
            print("Current Balance :", balance)

        elif n == 4:
            print("Transaction has completed...\nThank you visit again !!")
            break
        
        else:
            print("Incorrect value")
            
            
ATM()



##===Program(2) ATM machine in python (Verification system integration)===

def ATM():
    
    balance = 1000.0
    
    MPIN = int(input("Enter your MPIN : "))
    
    username = input("Enter your username: ")
    password = int(input("Create your password: "))
    
    user = {}
    
    user[username] = {
        "Password": password
    }
    
    print(user)
    
    choice = input("Do you want to login?(Y/N): ")
    
    if choice == "y" or choice == "Y":
        login_username = input("Username: ")
        login_password = int(input("Password: "))
        
        for key, value in user.items():
            if login_username == username and login_password == password:
                print("Logged in successfully, WELCOME")
                while True:
                                    
                            print("1. Show Balance")
                            print("2. Deposit Money")
                            print("3. Withdraw Money")
                            print("4. Exit")
                                    
                            option = int(input("Choose a option any one : "))
                                    
                            if option == 1:
                            # acc_balance = float(input("Enter the balance : "))
                            # balance += acc_balance
                                print("Welcome to SBI Bank ATM","\nYour Account Balance :", balance)
                                        
                            elif option == 2:
                                acc_balance = float(input("Enter the deposit balance : "))
                                balance += acc_balance
                                print("Dear Customer, A/c XXXXXX1234 debited for Rs", balance)
                                    
                            elif option == 3:
                                acc_balance = float(input("Enter the withdraw money : "))
                                balance -= acc_balance
                                print("Current Balance :", balance)
                            
                            elif option == 4:
                                print("Transaction has completed...\nThank you visit again !!")
                                break
                                    
                            else:
                                print("Incorrect value")  
            else:
                print("Invalid username or password!")
                
                            
ATM()
