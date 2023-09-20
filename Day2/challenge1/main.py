with open('file.txt', 'r') as file:
    data  = file.read()

code = ''
data = data.split(" ")
for i in range(len(data) - 1):
    first_num = data[i]
    if first_num == "Zero":
        num = 0
    if first_num == "One":
        num = 1
    elif first_num == "Two":
        num = 2
    elif first_num == "Three":
        num = 3
    elif first_num == "Four":
        num = 4
    elif first_num == "Five":
        num = 5
    elif first_num == "Six":
        num = 6
    elif first_num == "Seven":
        num = 7
    elif first_num == "Eight":
        num = 8
    elif first_num == "Nine":
        num = 9

    second_num = data[i+1]
    if second_num == "Zeros":
        code += str(num * "0")
    if second_num == "Ones":
        code += str(num * "1")
    elif second_num == "Twos":
        code += str(num * "2")
    elif second_num == "Threes":
        code += str(num * "3")
    elif second_num == "Fours":
        code += str(num * "4")
    elif second_num == "Fives":
        code += str(num * "5")
    elif second_num == "Sixs":
        code += str(num * "6")
    elif second_num == "Sevens":
        code += str(num * "7")
    elif second_num == "Eights":
        code += str(num * "8")
    elif second_num == "Nines":
        code += str(num * "9")

print(code)