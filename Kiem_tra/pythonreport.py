file1 = open("pre_a_ex3_exp.txt",'r')
file2 = open("pre_b_ex3_exp.txt",'r')
file3 = open("pre_c_ex3_exp.txt",'r')
file4 = open("final_ex3_exp.txt",'w')

sum_fail = 0
sum_pass = 0
sum_notcheck = 0
sum1 = 0
sum2 = 0
sum3 = 0

data1 = file1.readlines()
data2 = file2.readlines()
data3 = file3.readlines()


sum_fail += int(data1[0][-3:-1])+int(data2[0][-3:-1])+int(data3[0][-3:-1])
sum_pass += int(data1[1][-3:-1])+int(data2[1][-3:-1])+int(data3[1][-3:-1])
sum_notcheck += int(data1[2][-1])+int(data2[2][-3:-1])+int(data3[2][-3:])
sum1 += int(data1[0][-3:-1])+int(data1[1][-3:-1])+int(data1[2][-1])
sum2 += int(data2[0][-3:-1])+int(data2[1][-3:-1])+int(data2[2][-3:-1])
sum3 += int(data3[0][-3:-1])+int(data3[1][-3:-1])+int(data3[2][-3:])

file4.write("FAIL: "+str(sum_fail))
file4.write("\nPASS: "+str(sum_pass))
file4.write("\nNOTCHECK: "+str(sum_notcheck))
file4.write("\n**********")
file4.write("\nSUM1: "+str(sum1))
file4.write("\nSUM2: "+str(sum2))
file4.write("\nSUM3: "+str(sum3))

file1.close()
file2.close()
file3.close()
file4.close()

