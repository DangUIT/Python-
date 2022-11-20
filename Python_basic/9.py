password = input("Nhap password: ")
thuong = 0
hoa = 0
so = 0
ky_hieu = 0
space = 0
for i in password:
    if i==' ':
        space += 1
    elif i.isupper():
        hoa += 1
    elif i.islower():
        thuong += 1
    elif i.isnumeric():
        so += 1
    else: 
        ky_hieu += 1
if space != 0:
    print("Invalid")
else:
    if thuong*hoa*so*ky_hieu!=0:
        print("Mat khau rat manh")
    else:
        if thuong*hoa*so!=0 or thuong*hoa*ky_hieu!=0 or thuong*ky_hieu*so!=0 or ky_hieu*hoa*so!=0:
            print("Mat khau manh")
        else:
            if thuong*hoa!=0 or thuong*ky_hieu!=0 or thuong*so!=0 or hoa*so!=0 or hoa*ky_hieu!=0 or so*ky_hieu!=0:
                print("Mat khau vua")
            else:
                print("Mat khau yeu")
            