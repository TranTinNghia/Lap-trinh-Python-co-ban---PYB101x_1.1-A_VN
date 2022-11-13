a = [int(input("Nhập số: ")) for i in range(int(input("Nhập số giá trị trong list: ")))]
b = [j for j in a if j % 2 != 0]
if len(b) == 0:
    print([])
else:
    print(b)