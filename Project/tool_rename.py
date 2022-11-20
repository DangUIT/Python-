import os,sys,glob
argv  = sys.argv[1:]
input = argv[argv.index('-i')+1]
os.chdir(input)
print(os.getcwd())
for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_ext = f_ext.replace(".bin",".txt")
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)
