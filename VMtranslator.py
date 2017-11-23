import math
import os

temp_conter = 5

def R_for_segment(segment):
    r = ""
    if segment == 'temp':
        r = temp_conter
        # temp_conter += 1   file object !
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

def vm_to_asm(vm_line):
    print()
    line_as_list = vm_line.split(' ')
    if (len(line_as_list)) == 1:
        return aritmetics_commands(vm_line.strip())
    comannd , segment , i = line_as_list[0], line_as_list[1], line_as_list[2]
    if segment == 'constant':
        return constant_command(i)
    if segment == 'pointer':
        return pointer_command(comannd, i)
    return segment_command(comannd , segment , i)

def constant_command(i):
    line = []
    line.append("// push constant " +i)
    line.append( "@"+i)
    line.append("D=A")
    line.append("@SP")
    line.append("A=M")
    line.append("M=D")
    line.append("@SP")
    line.append("M=M+1")
    return line_lst_2_str(line)

def segment_command(commad , segment , i):
    line = []
    line.append("//"+commad+ segment + i)
    line.append("@" + i)
    line.append("D=A")
    line.append(R_for_segment(segment))
    line.append("D=M+D")
    if commad == 'push':
        line.append("A=D")
        line.append("D=M")
        line.append("@SP")
        line.append("M=M+1")
        return line_lst_2_str(line)
    if commad == 'pop':
        line.append("@R13")
        line.append("M=D")
        line.append("@SP")
        line.append("AM=M-1")
        line.append("D=M")
        line.append("@R13")
        line.append("A=M")
        line.append("M=D")
        return line_lst_2_str(line)

def pointer_command(command, i):
    return ""

def aritmetics_commands(command):
    line = []
    line.append("// "+command)
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


