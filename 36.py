n = int(input())
result = 0
a = 0
b = a + 1
for i in range(1,n+1):
    a = a + 1
    b = b + 1
    result = result + (a / b)
print(round(result,2))