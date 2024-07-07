def perform_operation(num1:float,num2:float,operation:str):
    match operation:
        case "add" :
            print(num1 + num2)   
        case "subtract" :  
            print(num1 - num2)
        case "multiply" :
            print(num1 * num2)
        case "divide" :
            if num1 and num2 > 0:
                print(num1 / num2)
            else:
                print("Cannot divide by zero.")
        case _ :
            print("Invalid operator")
    return