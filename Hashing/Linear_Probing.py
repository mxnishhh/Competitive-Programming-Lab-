def linear_probing(table, key):
    size = len(table)
    index = key % size

    while table[index] != -1:
        index = (index + 1) % size

    table[index] = key


table = [-1] * 10

linear_probing(table, 25)
linear_probing(table, 35)
linear_probing(table, 15)

print(table)