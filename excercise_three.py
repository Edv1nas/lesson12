def devide(number1: int, number2: int) -> None:
 
    try:
        devide_result = number1 / number2
        
        

    except ZeroDivisionError:
        print("Error, you are dividing by zero")

    else:
        print("Result: ", devide_result)
    

    # finally:
    #     print("Your are maybe right or wrong!")

number1 = int(input("Please enter first number: "))
number2 = int(input("Please enter second number: "))

devide(number1,number2)