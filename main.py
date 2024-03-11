class menu():
    def __init__(self, command):
        self.command = command

    @staticmethod
    def get_command(usr_inpt):
        menu.remove_space(usr_inpt)
    
    @staticmethod
    def format_string(inpt_str):
        fixed_str = ""
        for ch in inpt_str:
            if ch != ' ':
                fixed_str += ch
        lowered_fixed_str = fixed_str.lower()
        return (lowered_fixed_str)

while True:
    print("Please choose a type of file to read\n")
    print("Type html for .html file\nType xml for .xml\nType custom for custom language file\n")
    mode = input("Please enter your input: ")