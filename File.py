



# Constants

#Commands
C_ARITHMETIC = 0
C_PUSH = 1
C_POP = 2
C_LABEL = 3
C_GOTO = 4
C_IF = 5
C_FUNCTION = 6
C_RETURN = 7
C_CALL = 8

#Segments and Symbols
LCL = "local"
ARG = "argument"
THIS = "this"
THAT = "that"
TEMP = "temp"
POINTER = "pointer"
STATIC = "static"
CONST = "constant"

class File:
    """
    handles the parsing of single .vm file
    reads vm commands, parse it into lexical components and provides convenient
    access to these components
    ingnores all whitespaces and comments
    """



    def __init__(self, input_file):
        """
        opens the input file and gets ready to parse it
        :param input_file:
        """
        self.input_file = input_file
        self.output_file = []




    def translate_arithmetic(self, id):
        """
        :param id: id of line in input_file that contains arithmetic command
        :return: vm translated line
        """


    def translate_command(self, id):
        """

        :param id: id of line in input_file that contains push,pop,function
         or call command
        :return: vm translated line
        """














