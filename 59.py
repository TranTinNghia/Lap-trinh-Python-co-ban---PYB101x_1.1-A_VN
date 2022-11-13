n = int(input("Nhập số nguyên: "))
def check_abundant_number(n):
    a = [i for i in range(1,n) if n % i == 0]
    sum_a = 0
    for j in a:
        sum_a = sum_a + j
    if int(sum_a) > n:
        return True
    else:
        return False
print(check_abundant_number(n))