import ast

with open('file.txt', 'r') as file:
    data_str = file.read()

code = ''

data_list = ast.literal_eval(data_str)

for index, matrix in enumerate(data_list):
    found = False
    row_index = 0
    for row in matrix:
        row_index += 1
        if sum(row) < 2:
            code += f"r{row_index - 1}"
            found = True
            break
    
    if not found:
        for col_index in range(0 ,5):
            column = []
            for row_index in range(0 ,5):
                column.append(matrix[row_index][col_index]) 
            if sum(column) < 2:
                code += f"c{col_index}"
                break 
print(code)