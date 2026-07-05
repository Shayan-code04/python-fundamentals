

class DivisionByZeroError(Exception):
    """Custom exception for division by zero, with more context than the builtin."""
    def __init__(self, numerator):
        super().__init__(f"Cannot divide {numerator} by zero")
        self.numerator = numerator


def get_number(prompt):
    """Prompt user for a number, keep asking until valid float/int is entered."""
    while True:
        raw = input(prompt).strip()
        if raw == "":
            print("Error: Input cannot be empty. Try again.")
            continue
        try:
            value = float(raw)
            return value
        except ValueError:
            print(f"Error: '{raw}' is not a valid number. Try again.")


def get_operator(prompt):
    """Prompt user for an operator, validate it's one of the supported ones."""
    valid_ops = {"+", "-", "*", "/"}
    while True:
        op = input(prompt).strip()
        if op in valid_ops:
            return op
        print(f"Error: '{op}' is not a valid operator. Use one of {valid_ops}.")


def calculate(num1, op, num2):
    """
    Perform the calculation based on operator.
    Parameters only — no globals, no hardcoded values.
    Raises DivisionByZeroError on divide-by-zero instead of letting
    Python's ZeroDivisionError leak out uncontrolled.
    """
    try:
        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "*":
            return num1 * num2
        elif op == "/":
            if num2 == 0:
                raise DivisionByZeroError(num1)
            return num1 / num2
        else:
            raise ValueError(f"Unsupported operator: {op}")
    except TypeError as e:
        # Guards against non-numeric types slipping through
        raise TypeError(f"Invalid operand types for calculation: {e}")


def run_calculator():
    """Main loop: keeps calculator running until user chooses to exit."""
    print("=== Exception-Safe Calculator ===")
    print("Type 'q' at any prompt to quit.\n")

    while True:
        try:
            num1_raw = input("Enter first number (or 'q' to quit): ").strip()
            if num1_raw.lower() == "q":
                print("Exiting calculator. Goodbye.")
                break

            # Reuse get_number logic but allow quit check first
            try:
                num1 = float(num1_raw)
            except ValueError:
                print(f"Error: '{num1_raw}' is not a valid number.\n")
                continue

            op = get_operator("Enter operator (+, -, *, /): ")
            num2 = get_number("Enter second number: ")

            result = calculate(num1, op, num2)

        except DivisionByZeroError as e:
            print(f"Math Error: {e}\n")
        except TypeError as e:
            print(f"Type Error: {e}\n")
        except ValueError as e:
            print(f"Value Error: {e}\n")
        except KeyboardInterrupt:
            print("\nCalculator interrupted by user. Exiting safely.")
            break
        except Exception as e:
            # Last-resort catch: log it, never let the program crash raw
            print(f"Unexpected error occurred: {type(e).__name__}: {e}\n")
        else:
            print(f"Result: {num1} {op} {num2} = {result}\n")
        finally:
            pass  # placeholder — could log attempt count here if extended


if __name__ == "__main__":
    run_calculator()