import random
dict = {0: 'keo', 1: 'bua', 2: 'bao'}
while True:
    x = int(input())
    if x<0 or x>2:
        print("Invalid")
    else:   
        break
computer = random.randint(0,2)
print("Nguoi: ",dict[x])
print("May: ",dict[computer])
if x == 0: 
    if computer == 0:
        print("Hoa")
    elif computer == 1:
        print("May thang")
    else:
        print("Nguoi thang")
elif x == 1:
    if computer == 0:
        print("Nguoi thang")
    elif computer == 1:
        print("Hoa")
    else:
        print("May thang")
else:
    if computer == 0:
        print("May thang")
    elif computer == 1:
        print("Nguoi thang")
    else:
        print("Hoa")