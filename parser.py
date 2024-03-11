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
        "<head>","</head>",
        "<body>","</body>",
        "<title>","</title>",
        "<h1>","</h1>",
        "<p>","</p>",
        "html","/html",
        "<ul>","</ul>",
        "<li>","</li>",
        "<a>","</a>"]
        # Close the file
        file.close()
    @staticmethod
    def xml_build():
        pass
    @staticmethod
    def custom_build():
        pass
