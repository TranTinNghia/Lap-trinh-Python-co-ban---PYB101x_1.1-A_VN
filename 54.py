a = int(input())
b = int(input())
c = int(input())
if (a == b) and (b == c):
    print("Equilateral triangle")
elif (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
    print("Isosceles triangle")
else:
    print("Scalene triangle")