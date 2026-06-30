def flatten_list(nested):
    """Flattens a list of lists into a single flat list using nested loops."""
    flat = []
    for sublist in nested:
        for item in sublist:
            flat.append(item)
    return flat

def flatten_list_comp(nested):
    """Flattens a list of lists into a single flat list using comprehension."""
    return [item for sublist in nested for item in sublist]

nested = [[1, 2], [3, 4], [5, 6]]
print(flatten_list(nested))
print(flatten_list_comp(nested))