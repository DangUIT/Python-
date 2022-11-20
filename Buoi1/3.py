a = int(input("Nhap a: "))
res = 0
if (a < 2):
    print("Khong la so nguyen to")
elif (a >= 2 and a < 4):
    print("La so nguyen to")
else:
    for i in range(2, a):
        if (a % i == 0):
            res += 1
            print("khong la so nguyen to")
            break
if (res == 0):
    print("La so nguyen to")
