res = int(input("Nhập số phần tử trong list: "))
a = [int(input("Nhập số: ")) for i in range(res)]
b = [int(j) for j in a if j % 2 == 0]
print(b)