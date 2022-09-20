import ITools
import Errors
import CPU
import CPU_logic
import GPU

file = ''
Reg_Var = {'ah': 0, 'ad' : 0, 'aox': 0, 'aoy': 0, 'aoc': '#fff', 'rrm':CPU.rom['0'], 'ti': 1000}
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
            if data[0].lower() == 'int': CPU.exec_int(self)
            elif data[0].lower() == 'mov': CPU.exec_mov(self)
            elif data[0].lower() == 'mkb': CPU.exec_mkb(self)
            elif data[0].lower() == 'pop': CPU.exec_pop(self)
            elif data[0].lower() == 'cmp': CPU.exec_cmp(self)

            elif data[0].lower() == 'add': CPU.exec_add(self)
            elif data[0].lower() == 'sub': CPU.exec_sub(self)
            elif data[0].lower() == 'mul': CPU.exec_mul(self)
            elif data[0].lower() == 'div': CPU.exec_div(self)

            elif data[0].lower() == 'lct': CPU.exec_sjl(self)
            elif data[0].lower() == 'jmp': CPU.exec_jmp(self)
            elif data[0].lower() == 'je': CPU.exec_je(self)
            elif data[0].lower() == 'jne': CPU.exec_jne(self)
            elif data[0].lower() == 'jg': CPU.exec_jg(self)
            elif data[0].lower() == 'jge': CPU.exec_jge(self)
            elif data[0].lower() == 'jl': CPU.exec_jl(self)
            elif data[0].lower() == 'jle': CPU.exec_jle(self)

            elif data[0].lower() == 'and': CPU_logic.AND(self)
            elif data[0].lower() == 'nand': CPU_logic.NAND(self)
            elif data[0].lower() == 'or': CPU_logic.OR(self)
            elif data[0].lower() == 'xor': CPU_logic.XOR(self)
            elif data[0].lower() == 'not': CPU_logic.NOT(self)
            elif data[0].lower() == 'nor': CPU_logic.NOR(self)
            elif data[0].lower() == 'xnor': CPU_logic.XNOR(self)
            else: ITools.Error(self.name, Errors.VarUndefined,  self.data[0].lower())
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
        Run_Line(i)