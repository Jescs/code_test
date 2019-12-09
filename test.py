from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)  # 只取history值列
    # 提供了两端都可以操作的序列, 这意味着, 你可以在序列前后都执行添加或删除,
    # 当限制长度的deque增加超过限制数的项时, 另一边的项会自动删除
    for li in lines:
        if pattern in li:
            yield li,previous_lines # yield 进行迭代
            # 带yield的函数是一个生成器，而不是一个函数了，这个生成器有一个函数就是next函数，next就相当于“下一步”生成哪个数，
            # 这一次的next开始的地方是接着上一次的next停止的地方执行的，所以调用next的时候，生成器并不会从foo函数的开始执行，只是接着上一步停止的地方开始，然后遇到yield后，return出要生成的数，此步就结束。
        previous_lines.append(li)


if __name__ == '__main__':
    with open('C:\\Users\\Administrator\\Desktop\\文件\\doc\\test.txt') as f:
        for line,previlines in search(f, 'runningdoctor', 5):
            for pline in previlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)