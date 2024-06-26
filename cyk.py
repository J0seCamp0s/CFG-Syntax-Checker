import xml.etree.ElementTree as ET

class CFG():
    @staticmethod
    def get_cfg(type):
        if type == 0:
            tree_iter = ET.iterparse('Xml_CFG.jff', events=('start', 'end'))
        if type == 1:
            tree_iter = ET.iterparse('Html_CFG.jff', events=('start', 'end'))
        if type == 2:
            tree_iter = ET.iterparse('MadeUp.jff', events=('start', 'end'))

        prod_rules = {'S':[]}
        left_arr = []

        currentElement = 'S'

        for event, element in tree_iter:
            if event == 'start':
                if element.tag == 'left':
                    if currentElement != element.text:
                        currentElement = element.text
                        prod_rules[currentElement] = []
                    left_arr.append(element.text)
                elif element.tag == 'right':
                    prod_rules[currentElement].append(element.text)
                    # Process the element here (e.g., extract data, analyze structure, etc.)
                element.clear()  # Clear the element from memory to conserve memory usage
        return prod_rules
    @staticmethod
    def cyk_algorithm(grammar, start_symbol, input_string, mode):
            table = CFG.initialize_table(input_string, grammar)
            CFG.fill_table(table, grammar)
            if mode == 0: 
                idxs = CFG.find_substring(input_string, grammar)
                CFG.print_parse(table,grammar,input_string,idxs)
            return start_symbol in table[0][-1]
        
    @staticmethod
    def find_substring(input_string, grammar):
        s_idx = 0
        exclude_idxs = []
        for idx, ch in enumerate(input_string):
            for nonterm in grammar:
                for prod in grammar[nonterm]:
                    if len(prod) > 1:
                        s_idx = 0
                        while s_idx < idx:
                            substring = input_string[s_idx:idx+1]
                            if substring == prod:
                                idxs = [s_idx, idx+1]
                                if idxs not in exclude_idxs:
                                    exclude_idxs.append(idxs)
                            s_idx += 1
        return(exclude_idxs)

    @staticmethod
    def get_substring_numb(input_string, sub_idxs):
        n = len(sub_idxs)
        size = len(input_string)
        total = 0
        if len(sub_idxs) == 0:
            return(len(input_string))
        for idxs in sub_idxs:
            sub_size = len(input_string[idxs[0]:idxs[1]])
            total = total + sub_size
        total = size - total
        n = n + total
        return(n)

    @staticmethod
    def initialize_table(input_string, grammar):
        sub_idxs = CFG.find_substring(input_string, grammar)
        n = CFG.get_substring_numb(input_string, sub_idxs)
        table = [[set() for _ in range(n)] for _ in range(n)]
        # Initialize the table with terminals derived directly from input symbols

        curr_idx = 0
        i = 0
        while curr_idx < len(input_string):
            substring = input_string[curr_idx]
            for idxs in sub_idxs:
                if idxs[0] == curr_idx:
                    substring = input_string[idxs[0]:idxs[1]]
                    curr_idx = idxs[1]
                    break
            for nonterm in grammar:
                if substring in grammar[nonterm]:
                    if grammar[nonterm] == "None":
                        print(f"None found{nonterm}")
                    table[i][i].add(nonterm)
            i+= 1
            if len(substring) == 1:
                curr_idx += 1
            if i == n:
                break
        return table

    @staticmethod
    def fill_table(table, grammar):
        n = len(table)
        write_r = 0
        write_c = 1
        next_c = 2
        while True:
            #assign values for the position of cell to compare
            c1_r = write_r
            c1_c = write_c
            c2_r = write_r
            c2_c = write_c
            #search for first non-empty cell in current row
            while table[c1_r][c1_c] == set():
                c1_c -= 1
                if c1_c == -1:
                    print("Empty Table!\n")
                    return(False)
            c1 = table[c1_r][c1_c]
            #search for frist non-empty cell in curren column
            while table[c2_r][c2_c] == set():
                c2_r += 1
                if c1_r == n:
                    print("Empty Table!\n")
                    return(False)
            c2 = table[c2_r][c2_c]
            #iterate through values at current cell c1
            for c1_val in c1:
                if c1_val == None:
                    continue
                #iterate through values at current cell c2
                for c2_val in c2:
                    if c2_val == None:
                        continue
                    #iterate through nonterminals
                    for nonterm in grammar:
                        #iterate through productions of nonterminal
                        for prod in grammar[nonterm]:
                            look_prod = c1_val + c2_val
                            if look_prod in prod:
                                table[write_r][write_c].add(nonterm)
            write_c += 1
            write_r += 1
            if write_c == n:
                if write_r == 1:
                    for row in table:
                        print(row)    
                    break
                write_c = next_c
                if next_c < n-1:
                    next_c = write_c + 1
                write_r = 0
    
    @staticmethod
    def print_parse(table, grammar, input_string, sub_idxs):
        n = len(table)
        read_r = 0
        read_c = n-1
        next_c =  read_c-1
        nonterm_arr = []
        if table[0][n-1] == set():
            print("Table Empty!/Error in parsing!\n")
            return(False)
        while True:
            if table[read_r][read_c] != set():
                c1_r = read_r
                c1_c = read_c-1
                c2_r = read_r+1
                c2_c = read_c
                #search for first non-empty cell in current row
                while table[c1_r][c1_c] == set():
                    c1_c -= 1
                    if c1_c == -1:
                        print("Empty Table!\n")
                        return(False)
                c1 = table[c1_r][c1_c]
                #search for frist non-empty cell in current column
                while table[c2_r][c2_c] == set():
                    c2_r += 1
                    if c1_r == n:
                        print("Empty Table!\n")
                        return(False)
                c2 = table[c2_r][c2_c]
                for nonterm in table[read_r][read_c]:
                    for c1_val in c1:
                        if c1_val == None:
                            continue
                        for c2_val in c2:
                            if c2_val == None:
                                continue
                            look_string = c1_val+c2_val
                            if look_string in grammar[nonterm]:
                                Current_nonterm = str(nonterm)
                                Current_len = len(Current_nonterm)
                                padding_border = ("----------------------")
                                padding_prod = ("")
                                for x in range(Current_len):
                                    padding_border += '-'
                                    padding_prod += ' '
                                print(f"{padding_border}")
                                print(f"  {padding_prod}{c2_val}")
                                print(f"{nonterm}--|")
                                print(f"  {padding_prod}{c1_val}")
                                print(f"{padding_border}")
            read_c += 1
            read_r += 1
            if read_c == n:
                read_c = next_c
                if next_c > 0:
                    next_c = read_c - 1
                read_r = 0
            if read_r == read_c:   
                break
        
        read_c = 0
        read_r = 0
        while True:
            cell = table[read_r][read_c]
            for nonterm in cell:
                nonterm_arr.append(nonterm)
            read_c += 1
            read_r += 1
            if read_c == n:
                break
        curr_idx = 0
        while curr_idx < len(input_string):
                substring = input_string[curr_idx]
                for idxs in sub_idxs:
                    if idxs[0] == curr_idx:
                        substring = input_string[idxs[0]:idxs[1]]
                        curr_idx = idxs[1]
                        break
                for nonterm in nonterm_arr:
                    if substring in grammar[nonterm]:
                        padding_border = ("----------------------")
                        padding_prod = ("")
                        for x in range(Current_len):
                            padding_border += '-'
                        print(f"{padding_border}")
                        print(f"{nonterm}--{substring}")
                        print(f"{padding_border}")
        for row in table:
            print(row) 