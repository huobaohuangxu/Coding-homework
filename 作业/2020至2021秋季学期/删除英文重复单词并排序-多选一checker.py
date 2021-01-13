'''删除英文重复单词并排序 http://oj.yangzhu.world/problem/rmreplsort
在一行内，从键盘输入若干个由空格分隔的英文单词（大小写敏感），
将这些单词去重后，按照字典序逆序输出，以元组（tuple）的形式输出'''
a = input()
c = []
b = a.split(' ')
for d in b:
    if d not in c:
        c.append(d)
c.sort(key=str.lower,reverse=True)
print(tuple(c))
