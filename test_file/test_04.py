# filename = 'pi_digits.txt'
#
#
# # with open(filename, 'w') as file_object:
# #     file_object.write('test')
#
# with open(filename, 'a') as file_object:
#     file_object.write('test \n')
#     file_object.write('test \n')
#
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())


try:
    print(5/0)
except ZeroDivisionError:
    print('You can\'t divide by zero')