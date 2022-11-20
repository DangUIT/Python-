def check_tong_uoc_so(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum += i
    return sum
a = []
for i in range(1,1001):
    if check_tong_uoc_so(i) == i:
        a.append(str(i))
print(','.join(a))
    
    