import sys
import os
import file_object

def main(path):
    """
    This fucntion classify the two options: .hack file path or directory path.
    This function calls the 'read_asm_file' and 'create_hack_file' function.
    """
    files = []
    if os.path.isfile(path):
        files.append(path)
    else:
        for f in os.listdir(path):
            f_path = ''.join([path,"/",f])
            if os.path.isfile(f_path):
                if str(f).split('.')[-1] == "vm":
                    files.append(f_path)
    for file_path in files:
        File = file_object.File(file_path)
        File.translate()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])



