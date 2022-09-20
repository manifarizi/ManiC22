import ITools
import Errors

def AND(self):
    (a, b) = self.data[1:2]
    if a == '0' or a == '1' and b == '0' or b == '1':
        if a == '1' and b == '1':
            self.Reg_Var['ax'] = True
        else:
            self.Reg_Var['ax'] = False
    else: ITools.Error(self.name, Errors.NotOneOrZero)

def NAND(self):
    (a, b) = self.data[1:2]
    if a == '0' or a == '1' and b == '0' or b == '1':
        if a == '1' and b == '1':
            self.Reg_Var['ax'] = False
        else:
            self.Reg_Var['ax'] = True
    else: ITools.Error(self.name, Errors.NotOneOrZero)

def OR(self):
    (a, b) = self.data[1:2]
    if a == '0' or a == '1' and b == '0' or b == '1':
        if a == '1' or b ==1:
            self.Reg_Var['ax'] = True
        else:
            self.Reg_Var['ax'] = False
    else: ITools.Error(self.name, Errors.NotOneOrZero)

def XOR(self):
    (a, b) = self.data[1:2]
    if a == '0' or a == '1' and b == '0' or b == '1':
        if a != b:
            self.Reg_Var['ax'] = '1'
        else:
            self.Reg_Var['ax'] = '0'
    else: ITools.Error(self.name, Errors.NotOneOrZero)

def NOT(self):
    a = self.data[1]
    if a == '0' or a == '1':
        if a != 1:
            self.Reg_Var['ax'] = '1'
        else:
            self.Reg_Var['ax'] = '0'
    else: ITools.Error(self.name, Errors.NotOneOrZero)

def NOR(self):
    (a, b) = self.data[1:2]
    if a == '0' or a == '1' and b == '0' or b == '1':
        if(a == '0') and (b == '0'):
            self.Reg_Var['ax'] = '1'
        elif(a == '0') and (b == '1'):
            self.Reg_Var['ax'] = '0'
        elif(a == '1') and (b == '0'):
            self.Reg_Var['ax'] = '0'
        elif(a == '1') and (b == '1'):
            self.Reg_Var['ax'] = '0'
    else: ITools.Error(self.name, Errors.NotOneOrZero)

def XNOR(self):
    (a, b) = self.data[1:2]
    if a == '0' or a == '1' and b == '0' or b == '1':
        if(a == b):
            self.Reg_Var['ax'] = '1'
        else:
            self.Reg_Var['ax'] = '0'
    else: ITools.Error(self.name, Errors.NotOneOrZero)
