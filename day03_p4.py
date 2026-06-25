def remove_duplicates_set(lst):
    return list(set(lst))

original = []
print("Enter 10 numbers:")
for i in range(10):
    num = int(input(f"Enter a number:{i+1} "))
    original.append(num)    


print(f"Original list: {original}")

print(f"Set method: {remove_duplicates_set(original)}")