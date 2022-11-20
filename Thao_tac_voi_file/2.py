output = []
with open("Exercises/bai_2.txt","r+") as file:
    data = file.readlines()
    for i in data:
        p = i[0:i.find('//')]
        if p !="":
            output.append(p)
    output = '\n'.join(output)
with open("Exercises/bai_2.txt","w") as file:
    file.write(output)

