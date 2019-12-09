from test_file.name_function import get_formatted_name

print("Enter 'q' at any time to quit")

while True:
    first = input("\nPlease give me a first name:")
    if first == 'q':
        break
    middle = input("Please give a middle name: ")
    if middle == 'q':
            break
    elif middle == '':
        last = input("Please give a last name: ")
        if last == 'q':
            break
    else:
        last = input("Please give a last name: ")
        if last == 'q':
            break
    if middle == '':
        formatted_name = get_formatted_name(first, last)
    else:
        formatted_name = get_formatted_name(first, last, middle)
    print("Neatly formatted name: {} .".format(formatted_name))
