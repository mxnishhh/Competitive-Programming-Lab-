
base = int(input("Enter base address: "))
i = int(input("Enter row index (i): "))
j = int(input("Enter column index (j): "))
n = int(input("Enter number of rows: "))
w = int(input("Enter size of each element in bytes: "))
address = base + ((j * n ) + i) * w

print("Address of A[", i, "][", j, "] =", address)