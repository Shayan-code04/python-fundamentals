names = [input("Enter name: ") for _ in range(5)]
scores = [int(input(f"Enter score for {name}: ")) for name in names]

# Build a list of tuples from two lists
score_data = list(zip(names, scores))

# Sort by score descending and take top 3
top3 = sorted(score_data, key=lambda x: x[1], reverse=True)[:3]

# Print unpacked tuples
for name, score in top3:
    print(name, score)
