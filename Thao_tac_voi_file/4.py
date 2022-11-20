with open("Exercises/bai_3.txt","r") as file:
    with open("Exercises/bai_4.txt","w") as file2:
        data = file.read()
        data = data.replace("x", ' ')
        lis = data.splitlines()
        for i in range(len(lis)):
            lis2 = lis[i].split()
            for i2 in range(len(lis2)):
                if lis2[i2].isdigit():
                    bir = bin(int(lis2[i2]))[2:].zfill(5)   
                    file2.write(bir+' ')
                else:
                    file2.write(lis2[i2]+' ')
            file2.write('\n')
            
    
