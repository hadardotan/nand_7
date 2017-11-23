import os, re

def open_path(path):
    """
    :param path:
    :return:
    """
    files = {}
    if os.path.isdir(path):
        dir = os.listdir(path)
        for ob in dir:
            if (not os.path.isdir(ob)) and (
            os.path.basename(ob).endswith(".vm")):
                name = os.path.basename(ob)
                vm_lines = read_vm_file(path + "\\" + name)
                files[name] = vm_lines
        return files, path
    else:
        name = os.path.basename(path)
        vm_lines = read_vm_file(path)
        files[name] = vm_lines
    return files, os.path.dirname(path)


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
            continue
        elif comment_start >0:
            line = line[:comment_start]
        new_lines.append(line)
    return new_lines

def get_asm_file_name(file_path):
    """

    :param file_path:
    :return:
    """
    file_name = re.sub(r'(\.vm)$', '', file_path)
    asm_file_name = file_name + ".asm"
    return asm_file_name

def read_vm_file(file_path):
    """
    This function returns a list of string, each string is a line from vm file.
    :param file_path
    :return: vm_lines
    """
    vm_file = open(file_path)
    vm_lines = []
    file_length = number_of_lines(file_path)
    for i in range(file_length):
        line = vm_file.readline()
        vm_lines.append(line)
    vm_file.close()
    vm_lines = clean_lines(vm_lines)
    return vm_lines

def number_of_lines(file_name):
    """
    This function return the lenght (of rows) of vm file
    :param file_name:
    :return: line_number
    """
    vm_file = open(file_name)
    line_number = 0
    while vm_file.readline():
        line_number += 1
    vm_file.close()
    return line_number
