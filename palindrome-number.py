n = int(input("Enter number: "))
copy = n
rev = 0

while n>0:
    digit = n%10
    rev = 10*rev + digit
    n //= 10

if copy == rev:
    print(copy, "is a palindrome number")
else:
    print(copy, "is not a palindrome number")