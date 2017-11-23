import VMtranslator

def clean_lines(vm_lines):
    """
    This function cleans all comments ("//") from lines
    :param vm_lines:
    :return: new_lines: cleaned list of vm lines
    """
    new_lines = []
    for i in range(len(vm_lines)):
        line = vm_lines[i].strip()
        comment_start = line.find("//")
        if line == "" or comment_start == 0:
            continue # TODO : check if continue or break
        elif comment_start >0:
            line = line[:comment_start]
        new_lines.append(line)
    return new_lines

def create_asm_file(asm_file_name, vm_lines):
    # variable_counter = 16
    # temp_counter = 5
    asm_file = open(asm_file_name, "w+")
    vm_lines = clean_lines(vm_lines)
    for vm_line in vm_lines:
        asm_file.write(VMtranslator.vm_to_asm(vm_line))
    asm_file.close()














