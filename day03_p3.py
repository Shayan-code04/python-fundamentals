
def max(lst):
    if len(lst) == 0:
        return None
    else:
        max_value = lst[0]
        for num in lst:
            if num > max_value:
                max_value = num
        return max_value
def min(lst):
    if len(lst)== 0:
        return None
    else:
        min_value = lst[0]
        for num in lst:
            if num < min_value:
                min_value = num
        return min_value
    
def average(lst):
    if len (lst) == 0:
        return None
    else:
        return sum(lst) / len(lst)
    
numbers = []
print("Enter numbers")
num = input("Enter a number (or 'done' to finish): ")
while num.lower() != 'done':
    try:
        number = float(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    num = input("Enter a number (or 'done' to finish): ")

print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")
print(f"Average: {average(numbers)}")