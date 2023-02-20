''' Create a function that takes one parameter as number - age , other as name which is default 'Anatnas', and some args and keywords.
Print first Name with age;
And then print all arguments with key arguments.'''


def print_name_age_with_arguments(age: int, name: str ="Antanas", *args, **kwargs) -> None:

    print(f"Name: {name}, age: {age}")
    print(f"sold arguments: {args if args else 'arge have not been provided'}, key arguments: {kwargs if kwargs else 'kwargs have not been provided'}")


print_name_age_with_arguments (23, "Tom", 12, "Argument", street = "Gedimino")