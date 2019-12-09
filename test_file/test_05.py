# i = 0
# while i < 11:
#     print(i)
#     i += 1
# while True:
#     i = 0
#     for i in range(0,11):
#         print(i)
#         i += 1
#     break
# i = input()
# print(i)
# i = int(input())
# print(i)

# import re
#
#
# def is_number(num):
#     pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
#     result = pattern.match(num)
#     if result:
#         return True
#     else:
#         return False
#
#
# while True:
#     i = input("Enter Number:")
#     if i == 'q':
#         print('-----End----')
#         break
#     if is_number(i):
#         if type(eval(i)) == int:
#             i = int(i)
#             if i > 0:
#                 print('{} is positive number'.format(i))
#             elif i < 0:
#                 print('{} is negative number'.format(i))
#             elif i == 0:
#                 print('{} is Zero'.format(i))
#         else:
#             print('{} is decimals'.format(i))
#     else:
#         print('{} is a string'.format(i))

# str = input("Enter something:")
# for i in str:
#     print(i)

# while True:
#     for i in str:
#         print(i)
#     break

# lists = []
# # i = 0
# # while i < 5:
# #     list_num = input('enter number:')
# #     if list_num == 'q':
# #         break
# #     else:
# #         list_num = int(list_num)
# #         lists.append(list_num)
# #         print(lists)
# #         sum_num = sum(lists)
# #         print('sum:{}'.format(sum_num))
# #         i += 1

