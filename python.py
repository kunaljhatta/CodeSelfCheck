# Name - Kunal Jhatta 
# Description - This Program asks user to perform calculations, and print results.

prompt = input("SuperMathyboard> ")

operator = prompt.split(' ', 1)[0]

split_number_string = prompt.split(' ', 1)[1]

split_third_part = split_number_string.split(' ')[1]

y = split_number_string.split(' ')
y = [float(i) for i in y]