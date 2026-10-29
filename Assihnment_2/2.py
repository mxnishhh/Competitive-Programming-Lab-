n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

checked = set()
result = []

for num in arr:
    if num not in checked:
        result.append(num)
        checked.add(num)

print("List after removing duplicates:", result)