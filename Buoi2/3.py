a = input()
a = a.lower()
a = a.replace('a', '')
a = a.replace('y', '')
a = a.replace('u', '')
a = a.replace('e', '')
a = a.replace('o', '')
a = a.replace('i', '')
output = ''
for i in range(len(a)):
    output = output + '.'+a[i]
print(output)
