n = int(input("Enter number: "))
copy = n
m = 0

while n>0:
    digit = n%10
    m = 10*m + digit
    n //= 10

if copy == m:
    print(copy, "is a palindrome number")
else:
    print(copy, "is not a palindrome number")