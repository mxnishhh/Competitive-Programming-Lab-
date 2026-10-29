n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

target = int(input("Enter target sum: "))

seen = {}

for i in range(n):
    needed = target - arr[i]

    if needed in seen:
        print("Indices:", seen[needed], i)
        break

    seen[arr[i]] = i