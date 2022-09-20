import re

def read(file):
    with open(file, encoding='utf-8') as file_obj:
        data_all = file_obj.read()
    height = re.findall('%(.*[0-9])H%', data_all)
    data = data_all.replace(f'%{height}H%\n', '')
    dataname_list = [i for i in re.findall(';(.*?):\n', data)]
    data_line = '\n(.*)' * (int(height[0]))
    data_list = [i for i in re.findall(f':{data_line}\n;', data)]
    return {dataname_list[i]: data_list[i] for i in range(len(dataname_list))}