n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

arr.sort(reverse=True)

print("Array in descending order:", arr)

target = int(input("Enter number to search: "))

low = 0
high = n - 1
result = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        result = mid
        break
    elif arr[mid] > target:
        low = mid + 1
    else:
        high = mid - 1

print("Index:", result)