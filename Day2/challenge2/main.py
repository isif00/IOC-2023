with open('file.txt', 'r') as file:
    data = file.read()

data = str(data)

binary_code = ''
for i in data:
    if i == 'o':
        binary_code += '0'
    if i == ' ':
        binary_code += ' '
    if i == 'l':
        binary_code += '1'


bit_groups = binary_code.split()

result_string = ''

for group in bit_groups:
    ascii_code = int(group, 2)
    charachter = chr(ascii_code)
    result_string += charachter

print(result_string)