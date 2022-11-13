a = set(input("Nhập số nguyên: ").split())
b = [i for i in (input("Nhập lệnh remove và số cần remove: ").split()) if i.isdigit()]
for j in b:
    if j in a:
        a.remove(j)
    else: 
        continue
sum_result = 0
for m in a:
    sum_result = sum_result + int(m)
print(sum_result)