s1 = input()
s2 = input()
x = s1[0:2] + s2[2:]
s1 = s2[0:2] + s1[2:]
s2 = x
print(s1 + " " + s2)