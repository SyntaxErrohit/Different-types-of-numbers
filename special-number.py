n = int(input("Enter number: "))
copy = n
total = 0

while n > 0:
    f = 1
    digit = n%10
    for i in range(digit):
        f *= i + 1
    total += f
    n //= 10

if copy == total:
    print(copy, "is a special number")
else:
    print(copy, "is not a special number")