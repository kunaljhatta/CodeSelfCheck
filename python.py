# Name - Kunal Jhatta 
# Description - This Program asks user to perform calculations, and print results.

while True:
    prompt = input("SuperMathyboard> ")

    operator = prompt.split(' ', 1)[0]

    if operator  == "quit":
        break

    split_number_string = prompt.split(' ', 1)[1]

    split_third_part = split_number_string.split(' ')[1]

    y = split_number_string.split(' ')
    y = [float(i) for i in y]

    if operator == 'add':
        w = y[0] + y[1]
        print(w)
    elif operator == 'sub':
        w = y[0] - y[1]
        print(w)
    elif operator == 'mul':
        w = y[0] * y[1]
        print(w)
    elif operator == 'div' or split_third_part == 0 and operator == 'div':
        try:
            w = y[0] / y[1]
            print(w)
        except ZeroDivisionError:
            print("Can't divide by zero.")
    else:
        print("usage: add|sub|mul|div v0 v1")
        print("       quit")
