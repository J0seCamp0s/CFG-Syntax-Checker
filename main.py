from cyk import CFG

class menu():
    def __init__(self, command):
        self.command = command
    @staticmethod
    def get_command(usr_inpt):
        usr_inpt = menu.format_string(usr_inpt)
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
    def format_string(inpt_str):
        fixed_str = ""
        for ch in inpt_str:
            if ch != ' ':
                fixed_str += ch
        lowered_fixed_str = fixed_str.lower()
        print(lowered_fixed_str)
        return (lowered_fixed_str)
    @staticmethod
    def parse_file(path):
        file = open(path, 'r')
        # Read the file
        inpt_str = file.read()

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

        # Close the file
        file.close()
        return(formatted_string)
def main():
    while True:
        print("Please choose a type of file to read\n")
        print("Type html for .html file\nType xml for .xml\nType custom for custom language file\n")
        inpt_mode = input("Please enter your input: ")
        mode = menu.get_command(inpt_mode)
        Prodcutions = CFG.get_cfg(mode)
        path = input("Please enter the name of the file you want to read:")
        input_str = menu.parse_file(path)

if __name__ == "__main__":
    main()