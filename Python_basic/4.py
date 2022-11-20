a = input()
a = a.split(',')
b = []
for i in range(len(a)):
    if int(a[i])%2 ==0:
        b.append(a[i])
print(','.join(b))