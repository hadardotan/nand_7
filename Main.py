import sys
import os
from VMtranslator import read_vm_file, create_asm_file
import re




def main(path):

    files = []
    if path[-1] != '\\' and path[-1] != '/':
        files.append(path)
    else:
        for file in os.listdir(path):
            if os.path.isfile(path+file):
                if (str(file).split('.')[-1] == "asm"):
                    files.append(str(path+file))
    for f in files:
        vm_lines = read_vm_file(f)
        file_name = re.sub(r'(\.vm)$', '', f)
        asm_file_name = file_name + ".asm"
        create_asm_file(asm_file_name,vm_lines)




if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])