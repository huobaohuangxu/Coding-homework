'''删除英文重复单词 http://oj.yangzhu.world/problem/rmrepl
在一行内，从键盘输入若干个由空格分隔的英文单词（大小写敏感），
将这些单词去重后，按照输入的先后顺序，以元组（tuple）的形式输出'''
a = input()
for b in a[2:]:
    if 'a' <= b <= 'z' :
        print(ord(b),end=' ')
    else:
        str_input = b.encode('unicode_escape')
        str_input = str_input.decode("utf-8")
        str_input = str_input.replace("\\u", "")
        c = int(str_input, 16)
        d_result = hex(c)
        print(d_result,end=' ')
