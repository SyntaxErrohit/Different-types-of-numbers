n = int(input("Enter number: "))
copy = n
total = 0

while n > 0:
    digit = n%10
    total += digit**3
    n //= 10

if copy == total:
    print(copy, "is an armstrong number")
else:
    print(copy, "is not an armstrong number")