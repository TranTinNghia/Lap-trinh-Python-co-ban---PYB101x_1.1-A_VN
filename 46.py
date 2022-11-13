n = int(input("Nhập số giá trị trong list: "))
def tinh_tong(n):
    sum_result = 0
    a = [input("Nhập số: ") for i in range(n)]
    for j in a:
        sum_result = sum_result + int(j)
    return sum_result
print(tinh_tong(n))