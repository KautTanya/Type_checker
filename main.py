"""Type_checker"""


def type_checker(*types):
    """Type_checker"""
    def decorator(func):
        """Type_checker"""
        def wrapper(*args, **kwargs):
            """Type_checker"""
            print(type(types))
            print(type(args))
            flag = True
            for i in args:
                if type(i) not in types:
                    flag = False
                    break

            for i in kwargs.values():
                if type(i) not in types:
                    flag = False
                    break

            if not flag:
                raise TypeError("Incorrect argument type!")

            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@type_checker(int, str)
def add_numbers(a, b, c=0):
    """example"""
    return f"{a} + {b} + {c}"


print(add_numbers(8, 7, c=5))
