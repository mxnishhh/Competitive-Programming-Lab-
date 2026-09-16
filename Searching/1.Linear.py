# Linear Search
# Searches for an element one by one

arr = [10, 20, 30, 40, 50]

key = int(input("Enter element to search: "))

for i in range(len(arr)):

    if arr[i] == key:
        print("Element found at index:", i)
        break

else:
    print("Element not found")