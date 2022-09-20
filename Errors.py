def FileNotFound(_: str) -> "_Error":
    description = 'Plase Enter a Valid File Name'
    return "FileNotFound", description

def ArgError(_: str) -> "_Error":
    description = 'Please Add a FileName'
    return "ArgError", description

def IntValNotDefined(_: str) -> "_Error":
    description = 'Please Eenter a Valid IntVal'
    return "IntValNotInvalid", description

def VarUndefined(_: str) -> "_Error":
    description = 'The Variable is Undefined'
    return "VarUndefined", description

def IndexError(_: str) -> "_Error":
    description = 'IndexError'
    return "IndexError", description

def VarNotDefined(var: str) -> "_Error":
    description = 'Trying Acces to ' + [var if not var is None else ''][0] + " But It's Undefined"
    return "VarUndefined", description

def SyntaxError(_: str) -> "_Error":
    description = 'SyntaxError'
    return "SyntaxError", description

def NotHex(_: str) -> "_Error":
    description = 'Expected Hex Value'
    return "NotHexError", description

def NotOneOrZero(_: str):
    description = 'Value Needs to Be 0 or 1'
    return "NotOneOrZero", description