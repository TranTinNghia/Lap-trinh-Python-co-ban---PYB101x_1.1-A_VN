n = int(input("Nhập số nguyên: "))
a = [i for i in range(1,n) if n % i == 0]
sum_result = 0
for j in a:
    sum_result = sum_result + j
print(sum_result)
