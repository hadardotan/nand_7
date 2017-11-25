import re
import Parser

Sp = "SP"
Local = "LCL"
Argument = "ARG"
This = "THIS"
That = "THAT"
Temp = "5"
Static = "16"

class File(object):
    """
    handles the parsing of single .vm file
    reads vm commands, parse it into lexical components and provides convenient
    access to these components
    ingnores all whitespaces and comments
    """
    def __init__(self, file_path):
        """
        opens the input file and gets ready to parse it
        :param input_file:
        """
        self.vm_path = file_path
        self.vm_lines = Parser.path_to_lines(self.vm_path)
        self.asm_path = re.sub(r'(\.vm)$', '', self.vm_path) + ".asm"
        self.file_name = (re.split('(\w+)', self.vm_path))[-4]
        self.counter = 0

    def translate(self):
        asm_file = open(self.asm_path, "w+")
        lines = self.vm_lines
        for i in range(len(lines)):
            translated = self.vm_to_asm(lines[i])
            asm_file.write(translated)
        asm_file.close()

    def vm_to_asm(self, line):
        """
        translates vm line to asm code
        :param file: file object
        :param i: index of line in file to translate
        :return:
        """
        as_list = line.split(' ')
        if (len(as_list)) == 1:
            return self.aritmetics_commands(line.strip())
        command, segment, i = as_list[0], as_list[1], as_list[2]
        if segment == 'this' or segment == 'that':
            return self.this_that_command(command,segment,i)
        if segment == 'constant':
            return self.constant_command(i)
        if segment == "local" or segment == "argument":
            return self.local_argument_command(command, segment, i)
        if segment == 'temp':
            return self.temp_command(command, i)
        if segment == 'pointer':
            return self.pointer_command(command, i)
        if segment == 'static':
            return self.static_command(command, i)


    def this_that_command(self, command , segment , i):
        line = ["// " + command + " " + segment + " " + i]
        #line =[]
        ram = That
        if segment == 'this':
            ram = This
        line.append("@" + ram)
        line.append("D=M")
        line.append("@"+i)
        if command == 'push':
            line.append("A=D+A")
            line.append("D=M")
            line.append("@SP")
            line.append("A=M")
            line.append("M=D")
            line.append("@SP")
            line.append("M=M+1")
            return Parser.line_lst_2_str(line)
        if command == 'pop':
            line.append("D=D+A")
            line.append("@R13")
            line.append("M=D")
            line.append("@SP")
            line.append("AM=M-1")
            line.append("D=M")
            line.append("@R13")
            line.append("A=M")
            line.append("M=D")
            return Parser.line_lst_2_str(line)

    def constant_command(self,i):
        """
        generates asm code for constant vm command
        :param i:
        :return: string  of asm code for constant vm command
        """
        line = ["// push constant " + i]
        line.append("@" + i)
        line.append("D=A")
        line.append("@SP")
        line.append("A=M")
        line.append("M=D")
        line.append("@SP")
        line.append("M=M+1")
        return Parser.line_lst_2_str(line)

    def local_argument_command(self, command , segment , i):
        """
        generates asm code for segment vm command
        :param file: file object
        :param command:
        :param segment:
        :param i:
        :return:
        """
        line = ["// " + command + " " + segment + " " + i]
        line.append("@" + self.ram_for_segment(segment))
        line.append("D=M")
        line.append("@" + i)
        if command == 'push':
            line.append("A=D+A")
            line.append("D=M")
            line.append("@SP")
            line.append("A=M")
            line.append("M=D")
            line.append("@SP")
            line.append("M=M+1")
            return Parser.line_lst_2_str(line)
        if command == 'pop':
            line.append("D=D+A")
            line.append("@R13")
            line.append("M=D")
            line.append("@SP")
            line.append("AM=M-1")
            line.append("D=M")
            line.append("@R13")
            line.append("A=M")
            line.append("M=D")
            return Parser.line_lst_2_str(line)

    def temp_command(self, command , i):
        line = ["// " + command + " temp " + i]
        line.append("@" + self.ram_for_segment("temp"))  ### R5 for temp?
        line.append("D=M")
        index = int(self.ram_for_segment("temp")) + int(i)
        line.append("@" + str(index))      # D = 5 + i
        if command == 'push':
            line.append("A=D+A")
            line.append("D=M")
            line.append("@SP")
            line.append("A=M")
            line.append("M=D")
            line.append("@SP")
            line.append("M=M+1")
            return Parser.line_lst_2_str(line)
        if command == 'pop':
            line.append("D=D+A")
            line.append("@R13")
            line.append("M=D")
            line.append("@SP")
            line.append("AM=M-1")
            line.append("D=M")
            line.append("@R13")
            line.append("A=M")
            line.append("M=D")
            return Parser.line_lst_2_str(line)

    def pointer_command(self, command, i):
        ram = That
        if i == "0":
            ram = This
        line = ["// " + command + " pointer " + i]
        line.append("@" + ram)
        if command == 'push':
            line.append("D=M")
            line.append("@SP")
            line.append("A=M")
            line.append("M=D")
            line.append("@SP")
            line.append("M=M+1")
            return Parser.line_lst_2_str(line)
        if command == 'pop':
            line.append("D=A")
            line.append("@R13")
            line.append("M=D")
            line.append("@SP")
            line.append("AM=M-1")
            line.append("D=M")
            line.append("@R13")
            line.append("A=M")
            line.append("M=D")
            return Parser.line_lst_2_str(line)

    def static_command(self,command, i):
        line = ["//" + command + "static" + i]
        name = self.file_name + "." + i
        index = 16 + int(i)
        line.append("@" + str(index))
        if command == 'pop':
            line.append("D=A")
            line.append("@R13")
            line.append("M=D")
            line.append("@SP")
            line.append("AM=M-1")
            line.append("D=M")
            line.append("@R13")
            line.append("A=M")
            line.append("M=D")
            return Parser.line_lst_2_str(line)
        if command == 'push':
            line.append("D=M")
            line.append("@SP")
            line.append("A=M")
            line.append("M=D")
            line.append("@SP")
            line.append("M=M+1")
            return Parser.line_lst_2_str(line)

    def aritmetics_commands(self, command):
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
            return Parser.line_lst_2_str(line)
        if command == "eq":
            return self.eq_command()
        if command == "gt" or command == "lt": ####
            return ""
        line.append("@SP")
        line.append("AM=M-1")
        line.append("D=M")
        line.append("A=A-1")
        if command == "add":
            line.append("M=M+D")
        if command == "sub":
            line.append("M=M-D")
        if command == "and":
            line.append("M=D&M")
        if command == "or":
            line.append("M=D|M")
        return Parser.line_lst_2_str(line)

    def ram_for_segment(self, segment):
        if segment == 'temp':
            return Temp
        if segment == 'local':
            return Local
        if segment == 'argument':
            return Argument
        if segment == 'this':
            return This
        if segment == 'that':
            return That
        if segment == 'static':
            return Static


    def eq_command(self):
        line = ["// eq"]
        line.append("@SP")
        line.append("AM=M-1")
        line.append("D=M")
        line.append("A=A-1")
        line.append("D=M-D")
        line.append("@FALSE"+str(self.counter))
        line.append("D;JNE")
        line.append("@SP")
        line.append("A=M-1")
        line.append("M=-1")
        line.append("@CONTINUE"+str(self.counter))
        line.append("0;JMP")
        line.append("(FALSE"+str(self.counter)+")")
        line.append("@SP")
        line.append("A=M-1")
        line.append("M=0")
        line.append("(CONTINUE"+str(self.counter)+")")
        self.counter +=1
        return Parser.line_lst_2_str(line)












