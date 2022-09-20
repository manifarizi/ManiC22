import sys
import ITools
import Errors
import Runner

try:
    file_name = sys.argv[1]
    with open(file_name, encoding='utf-8') as file:
        file_data = file.read()
except FileNotFoundError:
    ITools.Error('<Reader>', Errors.FileNotFound)
except IndexError:
    ITools.Error('<Reader>', Errors.ArgError)
else:
    Runner.Run(file_name, file_data, 0)