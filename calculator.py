def calculator():
    """
    The function `calculator` takes user input for an expression, evaluates it, stores the calculation
    history in a file, and provides options to view history, clear history, recalculate, or exit the
    program.
    :return: The `calculator()` function returns a message thanking the user for using the calculator.
    """
    # Input the expression:->
    print('\n<========== Welcome to Calculator ==========>')
    expression = input("Enter Your Expression:-> ")
    
    # Add Calculations into History.txt file:->
    with open("History.txt","a") as file:
            try:
                ans = str(eval(expression))
                file.write(f"{expression} = {ans}\n")
            except NameError:
                return "Invalid Expression!"
            except SyntaxError:
                return "Invalid Expression!"
            except ZeroDivisionError:
                return "Division by zero is not allowed!"
            except TypeError:
                return "Invalid Expression!"
    print(f"Your Answer is:-> {ans}")
            
    while True:
        print(f"\n{40*'='}\n")

        # Taking User's Choice as an Input:->
        choice = input("Press 1 to view Calculation History\nPress 2 to clear Calculation History\nPress 3 to Exit the Program\nPress 4 to Recalculate:-> ")
        
        # Printing the content of History.txt file:->
        if choice == "1":
            with open("History.txt","r") as file:
                content = file.read()
                print(f"\n{40*'='}\n\nHere's your Calculation History:->\n{content}")
    
        # Cleanning the content of History.txt file:->
        elif choice == "2":
            f = open("History.txt","r+")
            f.truncate(0)
            print(f"\n{40*'='}\n\nFinally your Calculation History has been successfully cleaned...")
            f.close()
    
        # Exit the Program:->  
        elif choice == "3":
            print(f"\n{40*'='}\n\nFinally your program has been successfully closed")
            break

        # Recalculate
        elif choice == "4":
            print(f"\n{40*'='}")
            expression = input("\nEnter Your Expression:-> ")
            try:
                ans = str(eval(expression))
            except NameError:
                return "Invalid Input!"
            except ValueError:
                return "Invalid Input!"
            print(f"Your answer is:-> {ans}")
            
            with open("History.txt","a") as file:
                file.write(f"{expression} = {ans}\n")

        # In the case of Invalid Input prints "Invalid Input!"
        else:
            print("Invalid Input!")
    return "Thanks for using this Calculator....."

print(calculator())