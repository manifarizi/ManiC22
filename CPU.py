import string
import sys
import time
import ROM
import ITools
import Errors
import Runner
import GPU

sys.setrecursionlimit(sys.getrecursionlimit() + 2500)

rom = ROM.read('ROM.ROM')

def get_item(self, item):
    global rom
    if item in self.Reg_Var:
        return self.Reg_Var[item]
    elif all(True if i in string.digits + '-' else False for i in item):
        return int(item)
    elif str(item).startswith('0x'):
        try:
            return int(item, base=16)
        except:
            ITools.Error(self.name, Errors.NotHex)

    elif str(item).startswith('$!'):
        if str(chr(int(get_item(self, item[2:])))) in rom:
            return rom[str(chr(int(get_item(self, item[2:]))))]
        else:
            ITools.Error(self.name, Errors.NotHex)

    elif str(item).startswith('$'):
        if str(item)[1:] in rom:
            return rom[str(item)[1:]]
        else:
            ITools.Error(self.name, Errors.NotHex)

    elif str(item).startswith('#'):
        try:
            return str(item)
        except IndexError:
            pass
    else:
        ITools.Error(self.name, Errors.VarNotDefined, item)

def draw_tool(Reg_Var, name):
    GPU.task_list.append((int(Reg_Var["aox"]), int(Reg_Var["aoy"]), str(Reg_Var["aoc"]), name))

def draw(self):
    if "aox" in self.Reg_Var and "aoy" in self.Reg_Var and "aoc" in self.Reg_Var:
        draw_tool(self.Reg_Var, self.name)
        GPU.task()
    else:
        ITools.Error(self.name, Errors.VarNotDefined, 'aox, aoy, aoc')

def drawrom(self):
    if "rrm" in self.Reg_Var and "aox" in self.Reg_Var and "aoy" in self.Reg_Var and "aoc" in self.Reg_Var:
        for ye, y in enumerate(self.Reg_Var['rrm']):
            for xe, x in enumerate(y):
                if x == '@':
                    draw_tool({'aox': int(xe + self.Reg_Var['aox']), 'aoy':  int(ye + self.Reg_Var['aoy']), 'aoc': str(self.Reg_Var['aoc'])}, self.name)
        GPU.task()
    else:
        ITools.Error(self.name, Errors.VarNotDefined, 'rrm, aox, aoy, aoc')

def exit_a(self):
    sys.exit(2)

def sleep(self):
    try:
        GPU.wait(int(self.Reg_Var['ti']))
    except TypeError:
        pass
    except KeyError:
        ITools.Error(self.name, Errors.VarNotDefined, 'ti')

def key_get(self):
    self.lc = [GPU.key[0], self.Reg_Var['ah'], 'cmp']

def key_get_num(self):
    self.Reg_Var['ad'] = GPU.key[0]

def clear(self):
    GPU.task_list = []
    GPU.task()

int_val = {'10': draw, '21': drawrom, '4': GPU.run, '128': exit_a, '8': key_get, '32': sleep, '16': key_get_num, '2': clear}

def exec_int(self):
    if str(get_item(self, self.data[1])) in int_val:
        int_val[str(get_item(self, self.data[1]))](self)
    else:
        ITools.Error(self.name, Errors.IntValNotDefined)

def exec_mov(self):
    if self.data[1] in self.Reg_Var:
        self.Reg_Var[self.data[1]] = get_item(self, self.data[2])
    else:
        ITools.Error(self.name, Errors.VarNotDefined, self.data[1])

def exec_mkb(self):
    if self.data[1] in self.Reg_Var:
        self.Reg_Var[self.data[1]] = get_item(self, self.data[2])
    else:
        try:
            self.Reg_Var.update({self.data[1]: get_item(self, self.data[2])})
        except IndexError:
            ITools.Error(self.name, Errors.IndexError)

def exec_pop(self):
    if self.data[1] in self.Reg_Var:
        del self.Reg_Var[self.data[1]]
    else:
        ITools.Error(self.name, Errors.VarNotDefined, self.data[1])

def exec_sjl(self):
    self.jmp_addr.update({self.data[1]: self.data[2]})

def jmp(self, addr):
    if addr in self.jmp_addr:
        Runner.Run(self.name[6:-3], self.file, self.jmp_addr[addr] + 1)
    else: ITools.Error(self.name, Errors.VarNotDefined, addr)

def exec_jmp(self):
    jmp(self, self.data[1])

def exec_add(self):
    if self.data[1] in self.Reg_Var:
        self.Reg_Var[self.data[1]] += get_item(self, self.data[2])
    else: ITools.Error(self.name, Errors.VarNotDefined, self.data[1])

def exec_sub(self):
    if self.data[1] in self.Reg_Var:
        self.Reg_Var[self.data[1]] -= get_item(self, self.data[2])
    else: ITools.Error(self.name, Errors.VarNotDefined, self.data[1])

def exec_mul(self):
    if self.data[1] in self.Reg_Var:
        self.Reg_Var[self.data[1]] *= get_item(self, self.data[2])
    else: ITools.Error(self.name, Errors.VarNotDefined, self.data[1])

def exec_div(self):
    if self.data[1] in self.Reg_Var:
        self.Reg_Var[self.data[1]] /= get_item(self, self.data[2])
    else: ITools.Error(self.name, Errors.VarNotDefined, self.data[1])

def exec_cmp(self):
    self.lc = [get_item(self, self.data[1]), get_item(self, self.data[2]), 'cmp']

def exec_je(self):
    if self.lc[0] == self.lc[1] and self.lc[2] == 'cmp':
        jmp(self, self.data[1])

def exec_jne(self):
    if not self.lc[0] == self.lc[1] and self.lc[2] == 'cmp':
        jmp(self, self.data[1])

def exec_jg(self):
    if self.lc[0] > self.lc[1] and self.lc[2] == 'cmp':
        jmp(self, self.data[1])

def exec_jge(self):
    if not self.lc[0] < self.lc[1] and self.lc[2] == 'cmp':
        jmp(self, self.data[1])

def exec_jl(self):
    if self.lc[0] < self.lc[1] and self.lc[2] == 'cmp':
        jmp(self, self.data[1])

def exec_jle(self):
    if not self.lc[0] > self.lc[1] and self.lc[2] == 'cmp':
        jmp(self, self.data[1])

def exec_not(self):
    if not self.data[1]:
        jmp(self, self.data[1])
