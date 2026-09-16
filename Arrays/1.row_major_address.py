# Find address of an element in a 2D array using Row-Major Order
# Row-major formula: Address = Base + ((i * number_of_columns) + j) * element_size

base = int(input("Enter base address: "))
i = int(input("Enter row index (i): "))
j = int(input("Enter column index (j): "))
n = int(input("Enter number of columns: "))
w = int(input("Enter size of each element in bytes: "))
address = base + ((i * n) + j) * w

print("Address of A[", i, "][", j, "] =", address)