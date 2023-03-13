from this import d


n = int(input("Enter number: "))
m = 0

while n>0:
    digit = n%10
    m = 10*m + digit
    n //= 10

if m == n:
    print(m, "is a palindrome number")
else:
    print(m, "is not a palindrom number")