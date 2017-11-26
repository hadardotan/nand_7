import sys
import os
import file_object

def main(path):
    """
    This fucntion classify the two options: .hack file path or directory path.
    This function calls the 'read_asm_file' and 'create_hack_file' function.
    """
    files = []
    if path[-1] != '\\' and path[-1] != '/':
        files.append(path)
    else:
        for f in os.listdir(path):
            if os.path.isfile(path+f):
                if (str(f).split('.')[-1] == "asm"):
                    files.append(str(path+f))

    for file_path in files:
        File = file_object.File(file_path)
        File.translate()


# if __name__ == "__main__":
#     if len(sys.argv) == 2:
#         main(sys.argv[1])

basic_test = r"C:\Users\mika\Desktop\nand2tetris\nand2tetris\projects\07\MemoryAccess\BasicTest\BasicTest.vm"
static = r"C:\Users\mika\Desktop\nand2tetris\nand2tetris\projects\07\MemoryAccess\StaticTest\StaticTest.vm"
simple_add = r"C:\Users\mika\Desktop\nand2tetris\nand2tetris\projects\07\StackArithmetic\SimpleAdd\SimpleAdd.vm"
point = r"C:\Users\mika\Desktop\nand2tetris\nand2tetris\projects\07\MemoryAccess\PointerTest\PointerTest.vm"
stack_test = r"C:\Users\mika\Desktop\nand2tetris\nand2tetris\projects\07\StackArithmetic\StackTest\StackTest.vm"


main(basic_test)
main(static)
main(simple_add)
main(point)
main(stack_test)



