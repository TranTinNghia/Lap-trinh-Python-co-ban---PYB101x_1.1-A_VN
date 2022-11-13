a = int(input())
b = int(input())
sum_value = 0
if a < b:
    for i in range(a,b+1):
        if i % 2 == 0:
            continue
        else:
            sum_value = sum_value + i
            i = i + 1
else:
    print("Unmet condition!")
print(sum_value)