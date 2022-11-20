with open("Exercises/bai_2.txt","r") as file:
    f = file.read()
    f = f.replace(',',' ')
    f = f.replace('(','x')
    f = f.replace(')',' ')
with open("Exercises/bai_3.txt","w") as file:
    file.write(f)