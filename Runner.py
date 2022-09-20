import ITools
import Errors
import CPU
import CPU_logic
import GPU

file = ''
Reg_Var = {'ah': '0', 'ad' : '0', 'aox': '0', 'aoy': '0', 'aoc': '#fff', 'rrm':CPU.rom['0'], 'ti': '1000'}
File_Name = ''
jmp_addr = {}
lc = [0, 0, 'empty']
class Run_Line():
    def __init__(self, data):
        global jmp_addr
        global Reg_Var
        global File_Name
        global file
        global lc
        self.data = data
        self.name = File_Name
        self.jmp_addr = jmp_addr
        self.Reg_Var = Reg_Var
        self.lc = lc
        self.file = file
        try:
            if data[0].lower().strip() == 'int': CPU.exec_int(self)
            elif data[0].lower().strip() == 'mov': CPU.exec_mov(self)
            elif data[0].lower().strip() == 'test': print(CPU.get_item(self, self.data[1]))
            elif data[0].lower().strip() == 'mkb': CPU.exec_mkb(self)
            elif data[0].lower().strip() == 'pop': CPU.exec_pop(self)
            elif data[0].lower().strip() == 'cmp': CPU.exec_cmp(self)

            elif data[0].lower().strip() == 'add': CPU.exec_add(self)
            elif data[0].lower().strip() == 'sub': CPU.exec_sub(self)
            elif data[0].lower().strip() == 'mul': CPU.exec_mul(self)
            elif data[0].lower().strip() == 'div': CPU.exec_div(self)

            elif data[0].lower().strip() == 'lct': CPU.exec_sjl(self)
            elif data[0].lower().strip() == 'jmp': CPU.exec_jmp(self)
            elif data[0].lower().strip() == 'je': CPU.exec_je(self)
            elif data[0].lower().strip() == 'jne': CPU.exec_jne(self)
            elif data[0].lower().strip() == 'jg': CPU.exec_jg(self)
            elif data[0].lower().strip() == 'jge': CPU.exec_jge(self)
            elif data[0].lower().strip() == 'jl': CPU.exec_jl(self)
            elif data[0].lower().strip() == 'jle': CPU.exec_jle(self)

            elif data[0].lower().strip() == 'and': CPU_logic.AND(self)
            elif data[0].lower().strip() == 'nand': CPU_logic.NAND(self)
            elif data[0].lower().strip() == 'or': CPU_logic.OR(self)
            elif data[0].lower().strip() == 'xor': CPU_logic.XOR(self)
            elif data[0].lower().strip() == 'not': CPU_logic.NOT(self)
            elif data[0].lower().strip() == 'nor': CPU_logic.NOR(self)
            elif data[0].lower().strip() == 'xnor': CPU_logic.XNOR(self)
            else: ITools.Error(self.name, Errors.VarNotDefined,  self.data[0].lower().strip())
        except IndexError:
            ITools.Error(self.name, Errors.IndexError)
        jmp_addr = self.jmp_addr
        lc = self.lc

def Run(name, data, index):
    global File_Name
    global file
    File_Name = f'[bold]{name}[/]'
    file = data
    for i in ITools.Tokenize(data, index):
        if not ''.join([str(d) for d in i]).strip() == '':
            Run_Line(i)