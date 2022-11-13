a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
def luy_thua(a,b):
    if a == 0:
        return 0
    elif (a == 1) or (b == 0):
        return 1
    else:
        return luy_thua(a,b-1) * a
print(luy_thua(a,b))