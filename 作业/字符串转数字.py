'''字符串转数字 http://oj.yangzhu.world/problem/stringtonum
从键盘输入一个字符串（只含有英文和中文），
将该字符串中第3个字符（含）之后的字符依次转换为对应的unicode编码数字输出
（英文输出10进制数，中文输出16进制数）'''
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
