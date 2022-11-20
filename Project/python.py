pc = -4
address = {}
types = {
'add'   : 'R',
'addw'  : 'R',
'addi'  : 'I',
'addiw' : 'I',
'and'   : 'R',
'andi'  : 'I',
'auipc' : 'U',
'beq'   : 'SB',
'bge'   : 'SB',
'bgeu'  : 'SB',
'blt'   : 'SB',
'bltu'  : 'SB',
'bne'   : 'SB',
'csrrc' : 'I',
'csrrci': 'I',
'csrrs' : 'I',
'csrrsi': 'I',
'csrrw' : 'I',
'csrrwi': 'I',
'jal'   : 'UJ',
'jalr'  : 'I',
'lb'    : 'I',
'lbu'   : 'I',
'lh'    : 'I',
'lhu'   : 'I',
'lui'   : 'U',
'lw'    : 'I',
'lwu'   : 'I',
'or'    : 'R',
'ori'   : 'I',
'sb'    : 'S',
'sh'    : 'S',
'sll'   : 'R',
'sllw'  : 'R',   
'slli'  : 'I',   
'slliw' : 'I',   
'slt'   : 'R',   
'slti'  : 'I',   
'sltiu' : 'I',   
'sltu'  : 'R',   
'sra'   : 'R',   
'sraw'  : 'R',   
'srai'  : 'I',   
'sraiw' : 'I',   
'srl'   : 'R',   
'srlw'  : 'R',   
'srli'  : 'I',   
'srliw' : 'I',   
'sub'   : 'R',   
'subw'  : 'R', 
'sw'    : 'S', 
'xor'   : 'R', 
'xori'  : 'I',     
}

opcode = {
'add'   : '0110011',
'addw'  : '0111011',
'addi'  : '0010011',
'addiw' : '0011011',
'and'   : '0110011',
'andi'  : '0010011',
'auipc' : '0010111',
'beq'   : '1100011',
'bge'   : '1100011',
'bgeu'  : '1100011',
'blt'   : '1100011',
'bltu'  : '1100011',
'bne'   : '1100011',
'csrrc' : '1110011',
'csrrci': '1110011',
'csrrs' : '1110011',
'csrrsi': '1110011',
'csrrw' : '1110011',
'csrrwi': '1110011',
'jal'   : '1101111',
'jalr'  : '1100111',
'lb'    : '0000011',
'lbu'   : '0000011',
'lh'    : '0000011',
'lhu'   : '0000011',
'lui'   : '0110111',
'lw'    : '0000011',
'lwu'   : '0000011',
'or'    : '0110011',
'ori'   : '0010011',
'sb'    : '0100011',
'sh'    : '0100011',
'sll'   : '0110011',
'sllw'  : '0111011',   
'slli'  : '0010011',   
'slliw' : '0011011',   
'slt'   : '0110011',   
'slti'  : '0010011',   
'sltiu' : '0010011',   
'sltu'  : '0110011',   
'sra'   : '0110011',   
'sraw'  : '0111011',   
'srai'  : '0010011',   
'sraiw' : '0011011',   
'srl'   : '0110011',   
'srlw'  : '0111011',   
'srli'  : '0010011',   
'srliw' : '0011011',   
'sub'   : '0110011',   
'subw'  : '0111011', 
'sw'    : '0100011', 
'xor'   : '0110011', 
'xori'  : '0010011',       
}

funct7 = {
'add'   : '0000000',
'addw'  : '0000000',
'and'   : '0000000',
'or'    : '0000000',
'sll'   : '0000000',
'slli'  : '0000000',
'sllw'  : '0000000',     
'slt'   : '0000000',     
'sltu'  : '0000000',   
'sra'   : '0100000',   
'sraw'  : '0100000',   
'srl'   : '0000000',
'srli'  : '0000000',
'srai'  : '0100000',
'srlw'  : '0000000',     
'sub'   : '0100000',   
'subw'  : '0100000', 
'xor'   : '0000000'   
}

funct3 = {
'add'   : '000',
'addw'  : '000',
'addi'  : '000',
'addiw' : '000',
'and'   : '111',
'andi'  : '111',
'beq'   : '000',
'bge'   : '101',
'bgeu'  : '111',
'blt'   : '100',
'bltu'  : '110',
'bne'   : '001',
'csrrc' : '011',
'csrrci': '111',
'csrrs' : '010',
'csrrsi': '110',
'csrrw' : '001',
'csrrwi': '101',
'jalr'  : '000',
'lb'    : '000',
'lbu'   : '100',
'lh'    : '001',
'lhu'   : '101',
'lw'    : '010',
'lwu'   : '110',
'or'    : '110',
'ori'   : '110',
'sb'    : '000',
'sh'    : '001',
'sll'   : '001',
'sllw'  : '001',   
'slli'  : '001',   
'slliw' : '001',   
'slt'   : '010',   
'slti'  : '010',   
'sltiu' : '011',   
'sltu'  : '011',   
'sra'   : '101',   
'sraw'  : '101',   
'srai'  : '101',   
'sraiw' : '101',   
'srl'   : '101',   
'srlw'  : '101',   
'srli'  : '101',   
'srliw' : '101',   
'sub'   : '000',   
'subw'  : '000', 
'sw'    : '010', 
'xor'   : '100', 
'xori'  : '100',     
}

reg ={
'x0'    :   '00000',
'x1'    :   '00001',
'x2'    :   '00010',
'x3'    :   '00011',
'x4'    :   '00100',
'x5'    :   '00101',
'x6'    :   '00110',
'x7'    :   '00111',
'x8'    :   '01000',
'x9'    :   '01001',
'x10'   :   '01010',
'x11'   :   '01011',
'x12'   :   '01100',
'x13'   :   '01101',
'x14'   :   '01110',
'x15'   :   '01111',
'x16'   :   '10000',
'x17'   :   '10001',
'x18'   :   '10010',
'x19'   :   '10011',
'x20'   :   '10100',
'x21'   :   '10101',
'x22'   :   '10110',
'x23'   :   '10111',
'x24'   :   '11000',
'x25'   :   '11001',
'x26'   :   '11010',
'x27'   :   '11011',
'x28'   :   '11100',
'x29'   :   '11101',
'x30'   :   '11110',
'x31'   :   '11111',
}
def to_bin(n,b):
    n = int(n)
    if n>=0:
        imm = bin(n)[2:].zfill(b)
    else:
        n = bin(-n-1)[2:].zfill(b)
        imm = ""
        for x in n:
          if x =='0':
            imm = imm + '1'
          else:
            imm = imm + '0'
    return imm
        
def R_type(ins):
    bir = ''
    Opcode = opcode[ins[0]]
    Funct7 = funct7[ins[0]]
    Funct3 = funct3[ins[0]]
    rs2 = reg[ins[3]]
    rs1 = reg[ins[2]]
    rd = reg[ins[1]]
    bir = Funct7 + rs2 + rs1 + Funct3 + rd + Opcode
    return bir
def I_type(ins):
    bir = ''
    if ins[0] == 'ecall':
        bir = '00000000000000000000000001110011'
    elif ins[0] == 'ebreak':
        bir = '00000000000100000000000001110011'
    elif ins[0] in list(('lb','lbu','lh','lhu','lw','lwu','jalr')):
        imm = to_bin(ins[2],12)
        rs1 = reg[ins[3]]
        Funct3 = funct3[ins[0]]
        rd = reg[ins[1]]
        Opcode =opcode[ins[0]]
        bir = imm + rs1 + Funct3 + rd + Opcode
    elif ins[0] in list(('addi','addiw','andi','ori','xori','slti','sltiu')):
        imm = to_bin(ins[3],12)
        rs1 = reg[ins[2]]
        Funct3 = funct3[ins[0]]
        rd = reg[ins[1]]
        Opcode =opcode[ins[0]]
        bir = imm + rs1 + Funct3 + rd + Opcode
    elif ins[0] in list(('slli','slliw','srai','sraiw','srli','srliw')):
        imm = to_bin(ins[3], 12)
        imm = funct7[ins[0]] + imm[7:]
        rs1 = reg[ins[2]]
        Funct3 = funct3[ins[0]]
        rd = reg[ins[1]]
        Opcode =opcode[ins[0]]
        bir = imm + rs1 + Funct3 + rd + Opcode
    return bir
def S_type(ins):
    bir = ''
    imm = to_bin(ins[2],12)[:7]
    rs2 = reg[ins[1]]
    rs1 = reg[ins[3]]
    Funct3 = funct3[ins[0]]
    imm2 = to_bin(ins[2],12)[7:]
    Opcode = opcode[ins[0]]
    bir = imm + rs2 + rs1 + Funct3 + imm2 + Opcode
    return bir
def SB_type(ins):
    bir = ''
    imm = int(address[ins[3]]) - pc
    imm = to_bin(imm, 13)
    imm1 = str(imm[0] + imm[2:8])
    rs2 = reg[ins[2]]
    rs1 = reg[ins[1]]
    Funct3 = funct3[ins[0]]
    imm2 = str(imm[8:12] + imm[1])
    Opcode = opcode[ins[0]]
    bir = imm1 + rs2 + rs1 + Funct3 + imm2 + Opcode
    return bir
def U_type(ins):
    bir = ''
    imm = to_bin(ins[2], 20)
    rd = reg[ins[1]]
    Opcode = opcode[ins[0]]
    bir = imm + rd + Opcode
    return bir
def UJ_type(ins):
    bir = ''
    imm = int(address[ins[2]]) - pc
    imm = to_bin(imm, 21)
    imm1 = imm[0] + imm[10:20] + imm[9] + imm[1:9]
    rd = reg[ins[1]]
    Opcode = opcode[ins[0]]
    bir = imm1 + rd + Opcode
    return bir
def Clean_code(filename1,filename2):
    file1= open(filename1,"r")
    data = file1.readlines()
    file1.close()
    file2 = open(filename2,"w")
    for i in range(len(data)):
        if data[i].find("//") != -1:
            data[i] = data[i][:data[i].find("//")]
        if data[i].find("#") != -1:
            data[i] = data[i][:data[i].find("#")]
        data[i] = data[i].replace(".text"," ")
        data[i] = data[i].replace(".data"," ")
        data[i] = data[i].replace(","," ")
        data[i] = data[i].replace("("," ")
        data[i] = data[i].replace(")"," ")
        data[i]= data[i].split()
        if data[i]:
            for j in range(len(data[i])):
                file2.write(data[i][j] + ' ')
            file2.write("\n")     
    file2.close()

def Calculate_address(filename):
    global pc 
    pc = -4
    file1 = open(filename,"r")
    data1 = file1.readlines()
    file1.close()   
    for i in range(len(data1)):
        a = data1[i].split()
        if a[0].find(":") != -1:
            address.update( {a[0][:a[0].find(":")] : (pc+4)} )
            continue
        elif a[0].find(":") == -1:
            pc = pc + 4
    return address    
def Convert_Binary(filename):
    global pc
    pc = -4
    bir = ''
    file1 = open(filename,'r')
    data = file1.readlines()
    file1.close()
    file2 = open(filename,'w')
    for i in range(len(data)):
        a = data[i].split()
        if a[0].find(':') != -1:
            continue
        elif a[0].find(':') == -1:
            pc += 4
            if types[a[0]] == 'R':
                bir = R_type(a)
            elif types[a[0]] == 'I':
                bir = I_type(a)
            elif types[a[0]] == 'S':
                bir = S_type(a)
            elif types[a[0]] == 'SB':
                bir = SB_type(a)
            elif types[a[0]] == 'U':
                bir = U_type(a)
            elif types[a[0]] == 'UJ':
                bir = UJ_type(a)
        if bir:
            file2.write(bir + '\n')
    file2.close()
    
    
import sys, os , glob
argv = sys.argv[1:]
dir_inputfile = argv[argv.index('-i')+1:argv.index('-o')]
outputfile = argv[argv.index('-o')+1]
for inputfile in dir_inputfile:
    List = glob.glob(inputfile+'/**/*.S', recursive=True)
    for J in List:
        path_out = outputfile + J.replace(inputfile , '')
        path_out = path_out[:path_out.rfind("\\",0,len(path_out)-4)]
        os.makedirs(path_out,mode=0o777,exist_ok=True)
        file_output = path_out+ J[J.rfind('\\'):-1]+'txt'
        
        Clean_code(J,file_output)
        Calculate_address(file_output)
        Convert_Binary(file_output)
        
print("Completely Work")        

         

         
 
     
     

       





 
        






