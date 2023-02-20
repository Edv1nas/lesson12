from typing import Optional, Union

def divide(number: Union[float, int]) -> Union[float, int]:
    return number / 2 if isinstance(number, float) else number // 2

# try:
#     my_diveded_number = divide(0)
#     print(my_diveded_number)

# except:
#     print("oi ble")


# try:
#     magic_number = 2
#     my_diveded_number = divide(number=10)
#     print(my_diveded_number)
#     print(my_diveded_number / magic_number)
# except ZeroDivisionError:
#     print("my specific message for that exception")

# except Exception as e:
#     print(f" Error: {e}")

# else:
#     print("valio")
# finally:
    # print("yeeeeeeee")

# def physics_is_fun(temp_c: float, pressure_bar: float, time_utc: int, weight_kg:float) -> None:
#     pass

# physics_is_fun(temp_c=55.87, pressure_bar=26.58, time_utc=123456, weight_kg=458.4)


# def divide(number: Union[float, int]) -> Optional(Union[float, int]):
#     try:
#         return number / 2 if isinstance(number, float) else number // 2
#     except TypeError:
#         print("wrong type")
#     except Exception as e:
#         print(f" Error: {e}")
#     finally:
#         print("all good")



'''Examples'''        


from typing import Union
 #1. add numbers
def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    try:
        return a + b
    except TypeError:
        print("Please enter two numbers again. It must be a natural number or floating point numbers.")
    except Exception as e:
        print(f'Error: {e}')
# print(add_numbers(1, 4.2))
#2. personal info
def personal_info(first_name: str, last_name: str, age: int) -> Union[str, int]:
    try:
        return f"{first_name} {last_name} is {age} years old."
    except Exception as e:
        return f'Error: {e}'
# print(personal_info("Mary", 'Williams', age=5))
# #3. Make a list with numbers and power it by 3
def power_list(numbers: list) -> list:
    try:
        return [number ** 3 for number in numbers]
    except Exception as e:
        return f'Error: {e}'
# print(power_list([1, 2, 3, 4, '4']))
# 4. take two numbers and check if it's not divide by zero
def divide(first_num: Union[int, float], second_num: Union[int, float]) -> Union[int, float]:
    try:
        return first_num / second_num
    except ZeroDivisionError:
        return "Error: Division by zero"
# print(divide(2, 0))
# 5. This functions checks if number has a perfect square root
import math
def is_square(number: Union[int, float]) -> bool:
    try:
        return math.sqrt(number) % 1 == 0
    except Exception as e:
        return f'Error: {e}'
# print(is_square(25))


'''Example2'''

from typing import Optional
def greet_someone(name: str= "Human") -> Optional[str]:
    try:
        return f"Hello {name}"    
    except Exception as e:
        sys.exit(f"Error : {e}")
# print(greet_someone())def multiply_numbers(number_one: int | float, number_two: int | float ) -> Optional[int | float]:
    try:
        return number_one * number_two    
    except TypeError:
        print("Input is not a number")
# multiply("cat")def divide_numbers(number_one: int | float, number_two: int | float) -> Optional[float]:
    try:
        return number_one / number_two    
    except ZeroDivisionError:
        print("Divison by 0 is not available")
# divide(5,0)def verify_user(username: str) -> Optional[bool]:
    VALID_USERNAME = "Antanas"    
    try:
        if username == valid_username:
            return True        
        return False    
    except NameError:
        print("Name is not defined")
# print(verify_user("Antanas"))def uppercase_user_input() -> Optional[str]:
    try:
        user_input = input("Enter anything: ")
        return user_input.upper()
    except KeyboardInterrupt:
        print("\n Program stopped of keyboard interruption")
# print(uppercase_user_input())