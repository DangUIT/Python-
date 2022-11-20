a =input()
chu = 0
so = 0
for i in a:
    if i.isnumeric():
        so += 1
    if i.isalpha():
        chu += 1
print("Chu: ",chu," \nSo: ",so)
        