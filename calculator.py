while True:
    num1 = float(input("enter the first number: "))
    operation = input("choose(+,-,*,/,%): ")
    num2 = float(input("enter the second number: "))
    if operation == "/":
        if num2 == 0:
            print("can not divided by 0")
            continue
        result = num1/num2

    elif operation == "%":
        result = num1%num2 


    elif operation == "*":
        result = num1*num2 

    elif operation == "-":
        result = num1 - num2 

    elif operation == "+":   
        result = num1 + num2

    else:
        print("Invalide operation")
        continue

    print(f"the operation of {num1} and {num2} is {result}: ")


    game = input("do you want to calculate again?(y/n): ")
    if game.lower() == "y":
        print("welcome to game")
        continue
    if game.lower() == "n":
        print("byyyy")
    else:
        print("not a valid ans, so fuck you laterrrrr...") 
        continue
    break
    
    

    
           
    
    
                    
    

