# CFG-Syntax-Checker
This proyect is designed to check different strings against a defined set of Context Free Grammars.
The predefined Context Free Grammars are the following:
1. Html_CFG: This grammar is meant to represent a small set of basic tags in the HTML language.
2. Xml_CFG: This grammar is meant to represent tags and basic attributes of the XML language. 
3. MadeUp: This grammar is meant to represent a made-up programming language, that can execute some basic commands.
## Structure:
The proyect's code is spread throughout two files:
1. main.py: This file has the menu and basic instructions executed through the command prompt, such as reading
files and printing outputs.
2. cyk.py: This file has the CYK algorithm to parse the input string given by the user against the grammar selected in the menu. It also contains helper functions for the CYK algorithm. 