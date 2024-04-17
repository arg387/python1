exclude_numbers = {1, 3, 5}  # Use a set for faster membership testing

result = [i for i in range(1, 11) if i not in exclude_numbers]
print(" ", result)

print("Result Type:", type(result))

# Determine the type of each element in the result list
for item in result:
    print(f"Element Type: {type(item)}")

exclude_numbers = {1, 3, 5}
result = [str(i) for i in range(1, 11) if i not in exclude_numbers]
print(" ".join(result))
print("Result Type:", type(result))

# Determine the type of each element in the result list
for item in result:
    print(f"Element Type: {type(item)}")