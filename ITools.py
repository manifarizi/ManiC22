import rich
import re

class Error():
    def __init__(self, file_name: str, error_type: "function", description: str=None) -> None:
        rich.print(f'[red][bold]{error_type(description)[0]}[/] in {file_name} -> {error_type(description)[1]}')
        exit(2)

def Splitter(data, start) -> str:
    return data.split('\n')[start:len(data.split('\n'))]

def Tokenize(data: str, index: int) -> list:
    data_return = []
    for e, i in enumerate(Splitter(data, index)):
        if not i == '':

            if ':' in i:
                if i.strip()[0] == '_':
                    data_return.insert(0, ['lct', i[0:-1], e])
                else:
                    if ' db ' in i.lower():
                        after_d = re.findall(' db (.*)', (i + '\n').strip())[0]
                        data_return.append(['mkb', re.findall('(.*) db ', (i + '\n').strip())[0][0:-1], after_d])
            else:
                com = re.findall(';(.*?)\n', (i + '\n').strip())
                data_return.append(i.replace(', ', ' ').replace(',', ' ').replace([';' + com[0] if len(com) >= 1 else ''][0], '').strip().split(' '))
    return data_return