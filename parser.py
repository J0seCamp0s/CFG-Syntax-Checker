class CFG():
    def __init__(self, nonterminals,terminals, productions,start,inpt):
        self.nonterminals = nonterminals
        self.terminals = terminals
        self.productions = productions
        self.start = start
        self.inpt = inpt
    @staticmethod
    def html_build(path):
        # Open the file
        file = open(path, 'r')
        # Read the file
        inpt_str = file.read()
        html_terminals = [
        "html",
        "head",
        "meta",
        "title",
        "body",
        "list",
        "unordered",
        "ordered",
        "paragraph",
        "bold",
        "italic",
        "span",
        "br",
        "hr",
        "input",
        "form",
        "textarea",
        "links",
        "image",
        "anchor",
        "div"]
        # Close the file
        file.close()
    @staticmethod
    def xml_build():
        pass
    @staticmethod
    def custom_build():
        pass
