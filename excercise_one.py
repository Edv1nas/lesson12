'''1'''

# def addition(number1: int, number2: int) -> int:
#     sum = number1 + number2
#     return sum

# try:
#     numbers_sum = addition(number1=1, number2=15)
#     print(numbers_sum)

# except Exception as e:
#     print(f"Small error: {e}")

# else:
#     print(f"Sum = {numbers_sum}")

'''2'''

# from typing import List


# war_of_numbers = [44, 8, 19, 5]

# def value_return(new_list: List[int]) -> List:
#     even_num = []
#     odd_num = []
#     for num in new_list:
#         if (num % 2) == 0:
#             even_num.append(num)
#         else:
#             odd_num.append(num)

#     return sum(even_num) - sum(odd_num)
            
# try:
#     returned_number = value_return(new_list = ["a", 8, 19, 5])
#     print(returned_number)
# except TypeError:
#     print("Please enter int")
# except Exception as e:
#     print(f"Error: {e}")
# else:
#     print(f"Returned number: {returned_number}")
# finally:
#     print("all good but returned number maybe wrong!")

'''3'''
# from typing import Union

# def name_surname(name: str, surname: str) -> str:
#     return f"{name} {surname}"
# try:
#     name_print = name_surname(a,"Jonaitis")
#     print(name_print)

# except Exception as e:
#     print(f"Error: {e}")

'''4'''
from typing import Union

def number_divide(number_one: Union[int, float], number_two: Union[int, float]) -> Union:
    return number_one / number_two
try:
    devided_number = number_divide(10,1)
    print(devided_number)

except ZeroDivisionError:
    print("Error: Division by zero")







