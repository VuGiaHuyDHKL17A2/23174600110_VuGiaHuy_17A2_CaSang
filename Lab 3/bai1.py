while True:
    n = int(input("Nhập n là số nguyên dương: "))
    if n > 0:
        break
    print("Vui lòng nhập số nguyên dương")

# a
s1 = 0
for i in range(1,n+1):
    s1 += i

# b
s2 = 0
for i in range(1,n+1):
    s2 += 1 / i

# c
s3 = 0
for i in range(2,n+1):
    s3 += 1 / i**0.5
# d
s4 = 0
for i in range(1,n+1):
    s4 = ((-1) ** (i+1))/i

print(f"S1 = {s1}")
print(f"S2 = {s2}")
print(f"S3 = {s3}")
print(f"S4 = {s4}")