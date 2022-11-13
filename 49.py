n = int(input("Nhập số các giá trị trong list: "))
def get_unique_value(n):
    return [int(j) for j in dict.fromkeys([input("Nhập số: ") for i in range(n)]).keys()]
print(get_unique_value(n))
