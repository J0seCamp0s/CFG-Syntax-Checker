import xml.etree.ElementTree as ET

class CFG():
    @staticmethod
    def get_cfg(type):
        if type == 0:
            tree_iter = ET.iterparse('Xml_CFG.jff', events=('start', 'end'))
        if type == 1:
            tree_iter = ET.iterparse('Html_CFG.jff', events=('start', 'end'))
        if type == 2:
            tree_iter = ET.iterparse('Custom_CFG.jff', events=('start', 'end'))

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
    def cyk_algorithm(grammar, start_symbol, input_string):
        table = CFG.initialize_table(input_string, grammar)
        CFG.fill_table(table, grammar)
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
                
        return table

    @staticmethod
    def fill_table(table, grammar):
        n = len(table)
        start_row = 0
        start_col = n-1
        row_max = n
        write_r = 0
        write_c = 1
        row_offset = 0
        col_offset = 0
        while True:
            while table[start_row][start_col] == set():
                start_col = start_col - 1
                if start_col == -1:
                    print("Table empty\n")
                    return
            for row in table:
                print(row)
            print("\n")
            c1 = table[start_row][start_col]
            c1_row = start_row
            c1_col = start_col
            start_col = start_col +1
            #print(f"Current position of c1: [{c1_row}][{c1_col}]")
            while table[start_row][start_col] == set():
                start_row = start_row + 1
                if start_row == n:
                    return()
            c2 = table[start_row][start_col]
            c2_row = start_row
            c2_col = start_col
            #print(f"Current position of c2: [{c2_row}][{c2_col}]")
            for j in c1:
                    for k in c2:
                        for key in grammar.keys():
                            for prod in grammar[key]:
                                look_string = j+k
                                if look_string in prod:
                                    #print(f"Current j: {j}")
                                    #print(f"Current k: {k}")
                                    #print(f"Found match in: {key}")
                                    #print(f"Writting to: [{write_r + row_offset}][{write_c + col_offset}]\n")
                                    table[write_r + row_offset][write_c + col_offset].add(key)
            start_col = n-1
            if start_row == row_max-1:
                start_row = 0
                row_max -= 1
                write_c += 1
                row_offset = 0
                col_offset = 0
                #print("Diagonal finished\n")
            else:
                row_offset += 1
                col_offset += 1
                #print("Iteration finished\n")
            if row_max == 1:
                #print("Parse finish\n")
                break    

