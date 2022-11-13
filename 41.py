n = int(input())
s1 = []
s2 = []
for i in range(n):
    s1.append(int(input()))
for j in s1:
    if j % 5 == 0:
        s2.append(j)
    else:
        continue
if len(s2) == 0:
    print([0])
else:
    print(s2)