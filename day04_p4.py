nested = [[1, 2], [3, 4], [5, 6]]

# loop version
flat_list_loop = []
for sublist in nested:
    for item in sublist:
        flat_list_loop.append(item)

# comprehension version
flat_list_comp = [item for sublist in nested for item in sublist]

print(flat_list_loop)
print(flat_list_comp)
