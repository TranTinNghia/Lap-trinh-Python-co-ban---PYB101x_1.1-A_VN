n = input("Nhập chiều cao của 10 người: ")
a = set(n.split())
b = len(a)
sum_height = 0
for i in a:
    c = float(i)
    sum_height = sum_height + c
print(round(sum_height/b,2))