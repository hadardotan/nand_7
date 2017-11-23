import sys
import os
import VMtranslator
import re
import CodeWriter
import Parser


def main(path):
    files = []
    if path[-1] != '\\' and path[-1] != '/':
        files.append(path)
    else:
        for file in os.listdir(path):
            if os.path.isfile(path + file):
                if (str(file).split('.')[-1] == "vm"):
                    files.append(str(path + file))
    for f in files:
        vm_lines = Parser.read_vm_file(f)
        file_name = re.sub(r'(\.vm)$', '', f)
        asm_file_name = file_name + ".asm"
        CodeWriter.create_asm_file(asm_file_name, vm_lines)



####################################################################

# if __name__ == "__main__":
#     if len(sys.argv) == 2:
#         main(sys.argv[1])

####################################################################

def open_path(path):
    files = {}
    if os.path.isdir(path):
        dir = os.listdir(path)
        for ob in dir:
            if (not os.path.isdir(ob)) and (
            os.path.basename(ob).endswith(".vm")):
                name = os.path.basename(ob)
                vm_lines = Parser.read_vm_file(path + "\\" + name)
                files[name] = vm_lines
        return files, path
    else:
        name = os.path.basename(path)
        asm_lines = Parser.read_vm_file(path)
        files[name] = asm_lines
    return files, os.path.dirname(path)
example_path = r"C:\Users\mika\Desktop\nand2tetris\nand2tetris\projects\07\example folder"
files, folder_path = open_path(example_path)
for key in files.keys():
    name = key[:-4] + ".asm"
    asm_path = folder_path + "\\" + name
    CodeWriter.create_asm_file(asm_path,files[key])

####################################################################