

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("(((( YOU add sprinklesF))))")
        func(*args, **kwargs)
    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("(((((YOU add fudge)))))")
        func(*args, **kwargs)
    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")


get_ice_cream("vanilla")
