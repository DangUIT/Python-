hast_tab = {
	"addi" 	: "000",
	"sub"  	: "001",
	"sw"	: "010"
}
output = []
file1 = open("Exercises/bai_4.txt","r")
file2 = open("Exercises/bai_5.txt","w")
a = file1.readlines()
file1.close()
for i in range(len(a)):
    b = a[i].split()
    file2.write((hast_tab[b[0]]+b[1]+b[2]+b[3]).zfill(32))
    file2.write("\n")
file1.close()
file2.close()
    
