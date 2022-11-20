def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n-1)+fibo(n-2)


x = int(input("Nhap x: "))
if x < 1 or x > 30:
    print("So "+str(x)+" khong nam trong khoang [1,30]")
else:
    print(fibo(x))
