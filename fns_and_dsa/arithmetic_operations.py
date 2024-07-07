def perform_operation(num1, num2, operation):
    if operation == "add":
        print(num1 + num2)   
    
    elif operation == "subtract":  
        print(num1 - num2)
    
    elif operation == "multiply":
        print(num1 * num2)
    
    elif operation == "divide" :
        if num1 and num2 > 0:
            print(num1 / num2)
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid operator")
    return
perform_operation(1,3,"add")