# records = [('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4)]
#
#
# def do_foo(x, y):
#     print('foo', x, y)
#
#
# def do_bar(s):
#     print('bar', s)
#
#
# for tag, *args in records:
#     if tag == 'foo':
#         do_foo(*args)
#     elif tag == 'bar':
#         do_bar(*args)
#
# line = 'nobody:*:-2:-2:Unpri user:/var/EMPTY:/USR/BIN/FALSE'
# username,*args, path, userpath = line.split(':')
# print(username,*args,path,userpath)
items = [1, 3, 7, 5]

# def sum(items):
#     head, *tail = items
#     return head + sum(tail) if tail else head
#
#
# print(sum(items))
#
# head, *tail = items
# if tail:
#     sum_num = head +sum(tail)
#     print(sum_num)
# else:
#     sum_num = head
#     print(sum_num)
#
# from collections import deque
#
#
# def search(lines, pattern, history=5):
#     previous_lines = deque(maxlen=history)  # 只取history值列
#     # 提供了两端都可以操作的序列, 这意味着, 你可以在序列前后都执行添加或删除,
#     # 当限制长度的deque增加超过限制数的项时, 另一边的项会自动删除
#     for li in lines:
#         if pattern in li:
#             yield li  # yield 进行迭代
#             # 带yield的函数是一个生成器，而不是一个函数了，这个生成器有一个函数就是next函数，next就相当于“下一步”生成哪个数，
#             # 这一次的next开始的地方是接着上一次的next停止的地方执行的，所以调用next的时候，生成器并不会从foo函数的开始执行，只是接着上一步停止的地方开始，然后遇到yield后，return出要生成的数，此步就结束。
#         previous_lines.append(li)
#
#
# if __name__ == '__main__':
#     count = 0
#     with open('C:\\Users\\Administrator\\Desktop\\文件\\doc\\test.txt') as f:
#         for line in search(f, 'runningdoctor', 5):
#             print(line, end='')
#             count += 1
#             print('-' * 20)
#         print(count)

import heapq

nums = [13, 9, 1, 2, 3, 4, 5, 6, 7, 8]
# print(heapq.nlargest(5,nums))
# print(min(nums))
# print(max(nums))
# print(heapq.nsmallest(3,nums))
heapq.heapify(nums)
print(nums)