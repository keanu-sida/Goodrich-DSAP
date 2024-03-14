a = int(input("Enter a: \n"))
b = int(input("Enter b: \n"))
c = int(input("Enter c: \n"))

if ((a + b == c) or
    (a == b + c) or
    (a - b == c) or
    (a == b - c) or
    (a * b == c) or
    (a == b * c)):
    print("True!")
else:
    print("False!")
