#补考吗-ifelse http://oj.yangzhu.world/problem/makeupexam
#使用双分支结构完成程序。从键盘输入你的考试成绩（整数），若大于等于60分，输出“pass”，否则输出“retake exam”
grade=int(input())
if grade>=60:
    print("pass")
else:
    print("retake exam")
