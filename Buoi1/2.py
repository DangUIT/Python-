a = input()
b = 'true'
for i in range(len(a)):
    if (a[i] != a[len(a)-i-1]):
        print("F")
        b = 'false'
        break
if (b == 'true'):
    print("T")
