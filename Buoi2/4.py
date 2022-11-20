def check_number(a):
    for i in range(len(a)):
        global num_n, num_v, num_adj
        if a[i].endswith('lios') or a[i].endswith('liala'):
            num_adj += 1
        if a[i].endswith('etr') or a[i].endswith('etra'):
            num_v += 1
        if a[i].endswith('initis') or a[i].endswith('inites'):
            num_n += 1
    return (num_adj, num_n, num_v)


def check_gioi_tinh(a):
    name_male = []
    name_female = []
    for i in range(len(a)):
        if a[i].endswith("lios") or a[i].endswith("etr") or a[i].endswith("initis"):
            name_male.append(a[i])
        if a[i].endswith("liala") or a[i].endswith("etra") or a[i].endswith("inites"):
            name_female.append(a[i])
    if name_male == a or name_female == a:
        return "TRUE"
    return "FALSE"


def check_thu_tu(a):
    list_thu_tu = []
    for i in range(len(a)):
        if a[i].endswith("lios") or a[i].endswith("liala"):
            list_thu_tu.append(a[i])
        if a[i].endswith("etr") or a[i].endswith("etra"):
            list_thu_tu.append(a[i])
        if a[i].endswith("initis") or a[i].endswith("inites"):
            list_thu_tu.append(a[i])
    if list_thu_tu == a:
        return "TRUE"
    return "FALSE"


a = input("Nhap tu: ")
a = a.lower()
a = a.split()
num_n = 0
num_v = 0
num_adj = 0
(num_adj, num_n, num_v) = check_number(a)
if len(a) == 1 and (num_adj == 1 or num_v == 1 or num_n == 1):
    print("YES")
elif (num_adj == 0 and num_v == 0 and num_n == 0) or num_n >= 2:
    print("NO")
else:
    if check_gioi_tinh(a) == "TRUE" and check_thu_tu(a) == "TRUE":
        print("YES")
    else:
        print("NO")
