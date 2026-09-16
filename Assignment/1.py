n = int(input("Enter number of students: "))

attendance = []

for i in range(n):
    a = float(input("Enter attendance of student " + str(i + 1) + ": "))
    attendance.append(a)

threshold = float(input("Enter attendance threshold: "))

# 1. Count below threshold
count = 0
for a in attendance:
    if a < threshold:
        count += 1

# 2. Lowest attendance and position
lowest = attendance[0]
position = 0

for i in range(1, n):
    if attendance[i] < lowest:
        lowest = attendance[i]
        position = i

# 3. Average attendance
total = 0
for a in attendance:
    total += a

average = total / n

print("Students below threshold:", count)
print("Lowest attendance:", lowest)
print("Position:", position + 1)
print("Average attendance:", average)