

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
