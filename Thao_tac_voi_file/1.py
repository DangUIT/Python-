file = open("Exercises/bai_1.txt","r")
data = file.readlines()
file.close()
dtb = 0
file2 = open("Exercises/bai_1.txt","a")
for i in range(len(data)):
    data[i]=data[i].split()
    dtb += float(data[i][-1])
file2.write("\nDTB: "+str(dtb/3))
file2.close()


    
    
