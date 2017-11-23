import math
import os


class File(object):
    """
    handles the parsing of single .vm file
    reads vm commands, parse it into lexical components and provides convenient
    access to these components
    ingnores all whitespaces and comments
    """

    def __init__(self, input_file, asm_file_name):
        """
        opens the input file and gets ready to parse it
        :param input_file:
        """
        self.input_file = input_file
        self.temp_counter = 5
        self.variable_counter = 16
        self.asm_file_name = asm_file_name


    def get_line(self, i):
        """

        :param i: index of line
        :return: input_file[i]
        """
        return self.input_file[i]

    def get_asm_file_name(self):
        """

        :return: file name
        """
        return self.asm_file_name

    def get_temp_counter(self):
        """

        :return: temp_counter
        """
        return self.temp_counter

    def update_temp_counter(self):
        """
        sets temp_counter = num
        :param num: number
        :return:
        """
        self.temp_counter += 1

    def get_variable_counter(self):
        """

        :return:
        """
        return self.variable_counter

    def update_variable_counter(self):
        """

        :return:
        """
        self.variable_counter += 1

    def get_num_of_lines(self):
        """

        :return: number of vm file lines
        """
        return len(self.input_file)


def ram_for_segment(file, segment):
    """

    :param file:
    :param segment:
    :return:
    """
    r = ""
    if segment == 'temp':
        r = file.temp_counter
        file.update_temp_counter(file)
    if segment == 'local':
        r = "R1"
    if segment == 'argument':
        r = "R2"
    if segment == 'this':
        r = "R3"
    if segment == 'that':
        r = "R4"
    return r


def line_lst_2_str(line):
    str = ""
    for l in line:
        str += l
        str += "\n"
    return str


def vm_to_asm(file, i):
    """
    translates vm line to asm code
    :param file: file object
    :param i: index of line in file to translate
    :return:
    """

    vm_line = file.get_line(i)
    line_as_list = vm_line.split(' ')
    if (len(line_as_list)) == 1:
        return aritmetics_commands(vm_line.strip())
    command, segment, i = line_as_list[0], line_as_list[1], line_as_list[2]
    if segment == 'constant':
        return constant_command(i)
    if segment == 'pointer':
        return pointer_command(file, command, i) #TODO : i believe we'll need the object file here :)
    return segment_command(file, command , segment, i)


def constant_command(i):
    """
    generates asm code for constant vm command
    :param i:
    :return: string  of asm code for constant vm command
    """
    line = ["// push constant " + i, "@" + i, "D=A", "@SP", "A=M", "M=D",
            "@SP", "M=M+1"]
    return line_lst_2_str(line)


def segment_command(file, command , segment , i):
    """
    generates asm code for segment vm command
    :param file: file object
    :param command:
    :param segment:
    :param i:
    :return:
    """
    line = ["//" + command + segment + i, "@" + i, "D=A",
            ram_for_segment(file, segment), "D=M+D"]

    if command == 'push':
        line.append("A=D")
        line.append("D=M")
        line.append("@SP")
        line.append("M=M+1")
        return line_lst_2_str(line)
    if command == 'pop':
        line.append("@R13")
        line.append("M=D")
        line.append("@SP")
        line.append("AM=M-1")
        line.append("D=M")
        line.append("@R13")
        line.append("A=M")
        line.append("M=D")
        return line_lst_2_str(line)


def pointer_command(file, command, i):
    """

    :param file:
    :param command:
    :param i:
    :return:
    """
    return ""


def aritmetics_commands(command):
    """

    :param command:
    :return:
    """
    line = ["// " + command]
    if command == "neg" or command == "not":
        line.append("@SP")
        line.append("A=M")
        if command == "neg":
            line.append("D=-M")
        else:
            line.append("D=!M")
        line.append("M=D")
        return line_lst_2_str(line)
    if command == "eq" or command == "gt" or command == "lt": ####
        return ""
    line.append("@SP")
    line.append("AM=M-1")
    line.append("D=M")
    line.append("A=A-1")
    if command == "add":
        line.append("M=D+M")
    if command == "sub":
        line.append("M=D-M")
    if command == "and":
        line.append("M=D&M")
    if command == "or":
        line.append("M=D|M")
    return line_lst_2_str(line)


