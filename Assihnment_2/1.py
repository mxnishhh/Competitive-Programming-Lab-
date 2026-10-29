n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

result = 0

for num in arr:
    result = result ^ num

print("Single number:", result)