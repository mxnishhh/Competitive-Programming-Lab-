# Find offset of an element in Row-Major Order
#Offset = ((row x number of columns)+column) x element size

row = int(input("Enter row index: "))
col = int(input("Enter column index: "))

n = int(input("Enter number of columns: "))
w = int(input("Enter element size in bytes: "))

offset = ((row * n) + col) * w

print("Offset =", offset, "bytes")

base = int(input("Enter base address: "))

address = base + offset

print("Address =", address)