import math
import os
import parser


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
    if segment == 'temp':
        return temp_command(comannd, i)
    return segment_command(comannd , segment , i)


def aritmetics_commands(comannd):
    print()

def constant_command(i):  #push
    if i == 0:
        return ""
    return ""

def pointer_command(comannd, i):
    return ""

def temp_command(comannd, i):
    if i ==0:
        if comannd == 'push': #push 0
            return ""
        return ""  #pop 0
    if comannd == 'push':  #push i
        return ""
    return ""  #pop i

def segment_command(comannd , segment , i):
    if i ==0:
        if comannd == 'push': #push 0
            return ""
        return ""  #pop 0
    if comannd == 'push':  #push i
        return ""
    return ""  #pop i






