import math
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a+b <= c or a+c <= b or b+c <= a:
    print("Khong phai tam giac")
else:
    s = math.sqrt((a+b+c)*(a+b-c)*(b+c-a)*(c+a-b))/4
    if a == b == c:
        print("Tam giac deu, dien tich = "+str(s))
    elif a == b or a == c or b == c:
        print("Tam giac can, dien tich = "+str(s))
    elif a*a+b*b == c*c or a*a+c*c == b*b or b*b+c*c == a*a:
        print("Tam giac vuong, dien tich = "+str(s))
    else:
        print("Tam giac thuong, dien tich = "+str(s))

