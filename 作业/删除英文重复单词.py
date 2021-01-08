'''删除英文重复单词 http://oj.yangzhu.world/problem/rmrepl
在一行内，从键盘输入若干个由空格分隔的英文单词（大小写敏感），
将这些单词去重后，按照输入的先后顺序，以元组（tuple）的形式输出'''
a = input()
c = []
b = a.split(' ')
for d in b:
    if d not in c:
        c.append(d)
print(tuple(c))
