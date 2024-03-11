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
        html_nonterminals = [
        "S"
        "html",
        "head",
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
        html_terminals = [
        "<html>", "</html>",
        "<head>", "</head>",
        "<title>", "</title>",
        "<body>", "</body>",
        "<h1>", "</h1>",
        "<h2>", "</h2>",
        "<h3>", "</h3>",
        "<h4>", "</h4>",
        "<h5>", "</h5>",
        "<h6>", "</h6>",
        "<p>", "</p>",
        "<a>", "</a>",
        "<img>", 
        "<ul>", "</ul>",
        "<ol>", "</ol>",
        "<li>", "</li>",
        "<div>", "</div>",
        "<span>", "</span>",
        "<br>",  
        "<hr>",  
        "<strong>", "</strong>",
        "<em>", "</em>",
        "<input>", 
        "<form>", "</form>",
        "<textarea>", "</textarea>"
        ]
        html_prods = []
        # Close the file
        file.close()
    @staticmethod
    def xml_build():
        pass
    @staticmethod
    def custom_build():
        pass
