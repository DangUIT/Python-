import sys, os , glob
################ Lay duong dan folder
argv = sys.argv[1:]
dir_inputfile = argv[argv.index('-i')+1:]
################
################ Doi .S thanh .txt
for inputfile in dir_inputfile:
    List = glob.glob(inputfile+'/**/*.S', recursive=True)
    for J in List:
            K = J.replace(".S",".txt")
            os.rename(J, K)
    
    
    
####################### Doi lai nhu cu
'''for inputfile in dir_inputfile:
        List = glob.glob(inputfile+'/**/*.txt', recursive=True)
        for J in List:
            if "out" in J:
                K = J.replace(".txt",".S")
                os.rename(J, K)'''
        