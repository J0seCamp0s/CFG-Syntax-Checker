from cyk import CFG

class menu():
    def __init__(self, command):
        self.command = command
    @staticmethod
    def get_command(usr_inpt):
        usr_inpt = menu.format_string1(usr_inpt)
        accept_strings = ["xml","html","custom"]
        if usr_inpt not in accept_strings:
            print("Invalid input given!\nPlease try again.\n")
            return(-1)
        if usr_inpt == "xml":
            return(0)
        if usr_inpt == "html":
            return(1)
        if usr_inpt == "custom":
            return(2)
    @staticmethod
    def format_string1(inpt_str):
        fixed_str = ""
        for ch in inpt_str:
            if ch != ' ':
                fixed_str += ch
        lowered_fixed_str = fixed_str.lower()
        print(lowered_fixed_str)
        return (lowered_fixed_str)
    @staticmethod
    def format_string2(inpt_str):
        formatted_string = ""
        space_ignore = False
        for ch in inpt_str:
            if ch == '>':
                space_ignore = True
            if space_ignore:
                if ch == ' ' or ch == '\n' or ch == '\t':
                    continue
                if ch == '<':
                    space_ignore = False
            formatted_string += ch
        return(formatted_string)
    def format_string3(inpt_str):
        formatted_string = ""
        space_ignore = True
        for ch in inpt_str:
            if space_ignore:
                if ch == '(':
                    space_ignore = False
                if ch == ' ' or ch == '\n' or ch == '\t':
                    continue
            if ch == ')':
                space_ignore = True
            formatted_string += ch
        return(formatted_string)
    @staticmethod
    def parse_file(path,mode):
        try:
            file = open(path, 'r')
            # Read the file
            inpt_str = file.read()
            if mode == 0 or mode == 1:
                formatted_string = menu.format_string2(inpt_str)
            else:
                formatted_string = menu.format_string3(inpt_str)
            # Close the file
            file.close()
        except FileNotFoundError:
            print("File not found or cannot be accessed.\n")
            formatted_string = False
        return(formatted_string)
def main():
    while True:
        print("Please choose a type of file to read\n")
        print("Type html for .html file\nType xml for .xml\nType custom for custom language file\n")
        inpt_mode = input("Please enter your input: ")
        mode = menu.get_command(inpt_mode)
        if mode == -1:
            continue
        Prodcutions = CFG.get_cfg(mode)
        while True:
            path = input("Please enter the name of the file you want to read:")
            input_str = menu.parse_file(path,mode)
            if input_str == False:
                continue
            break
        #print(f"The file read is the following: {input_str}")
        result = CFG.cyk_algorithm(Prodcutions,'S',input_str,0)
        print(f"The result from parsing is the following: {result}")
        if result == True:
            while True:
                printing = input("Would you like to print the parsing tree?\nYes = 1\n No = 0\nPlease enter you input: ")
                if printing != 0 and printing != 1:
                    print("Invalid input! Please try again\n")
                elif printing == 0:
                    break
                elif printing == 1:
                    CFG.cyk_algorithm(Prodcutions,'S',input_str,1)

if __name__ == "__main__":
    main()