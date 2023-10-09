def decorate_as_string(func):

    def wrapper(*args, **kwargs):
        result = func(*args,**kwargs)
        return str(result)
    return wrapper

@decorate_as_string
def subtract(number1: int, number2: int) -> int:
    return number1 - number2


print(subtract(10,number2=24))
# print(type(subtract(10,24)))
