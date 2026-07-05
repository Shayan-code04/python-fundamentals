class Outofrangeerror(Exception):
    pass

def get_validated_input(promt,expected_type,min_value=None,max_value=None):
    while True:
        try:
            user_input = input(promt)
            if user_input.strip()=="":
                print("input cannot be empty.")
                continue
            value = expected_type(user_input)
            if min_value is not None and value < min_value:
                raise Outofrangeerror(f"value {value} is less than minimum allowed {min_value}.")
            if max_value is not None and value > max_value:
                raise Outofrangeerror(f"value {value} is greater than maximum allowed {max_value}.")
            return value
        except ValueError:
            print(f"invalid input. please enter a valid {expected_type.__name__}.try again.")
        except Outofrangeerror as e:
            print(e)
            

if __name__ == "__main__":

    age = get_validated_input(
        "Enter your age: ",
        int,
        min_value=1,
        max_value=120
    )

    price = get_validated_input(
        "Enter the product price: ",
        float,
        min_value=0
    )

    print("\nValidated Inputs")
    print(f"Age   : {age}")
    print(f"Price : {price}")

