a = input()
hoa = 0
thuong = 0
for i in a:
    if i.isupper():
        hoa += 1
    if i.islower():
        thuong += 1
print("Chu hoa: ",hoa," \nChu thuong: ",thuong)
        