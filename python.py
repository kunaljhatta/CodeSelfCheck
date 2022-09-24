# Name - Kunal Jhatta 
# Description - This Program asks user to perform calculations, and print results.

while True:
    prompt = input("SuperMathyboard> ")
    
    # Grabbing only the first string part of the user input
    operator = prompt.split(' ', 1)[0]
    
    # Quits the program if user enters quit 
    if operator  == "quit":
        break
    
    # This splits the number part of the string 
    split_number_string = prompt.split(' ', 1)[1]
    
    # This splits the last number part of the string 
    split_third_part = split_number_string.split(' ')[1]
    
    # Converting string of lists into numbers list 
    list = split_number_string.split(' ')
    list = [float(i) for i in list]

    if operator == 'add':
        sum = list[0] + list[1]
        print(sum)
    elif operator == 'sub':
        sum = list[0] - list[1]
        print(sum)
    elif operator == 'mul':
        sum = list[0] * list[1]
        print(sum)
    elif operator == 'div' or split_third_part == 0 and operator == 'div':
        try:
            sum = list[0] / list[1]
            print(sum)
        except ZeroDivisionError:
            print("Can't divide by zero.")
    else:
        print("usage: add|sub|mul|div v0 v1")
        print("       quit")
