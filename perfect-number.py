n = int(input("Enter number: "))
total = 0

for i in range(1,n):
    if n%i == 0:
        total += i

if total == n:
    print(n, "is a perfect number")
else:
    print(n, "is not a perfect number")