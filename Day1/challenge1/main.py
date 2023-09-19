import ast
from sympy import *


with open('file.txt', 'r') as file:
    data_str = file.read()

data_str = data_str.replace("combination", '"combination"').replace("sum", '"sum"')

data_list = ast.literal_eval(data_str)


for data in data_list:
    combination = data['combination']
    first_sum = data['sum']

    _sum = sum(combination)
    if  first_sum == _sum and isprime(_sum):
        print(f"combination:{combination}, sum:{first_sum}")
            
            



