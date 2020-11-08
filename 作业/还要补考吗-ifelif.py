#还要补考吗-ifelif http://oj.yangzhu.world/problem/makeupexam2
#使用if多分支结构完成程序。从键盘输入你的考试成绩（整数），若介于60到100分之间，输出“pass”，介于0到60分之间，输出“retake exam”，其他情况输出“input error”
grade=int(input())
if grade>=60 and grade<=100:
    print("pass")
elif grade>=0 and grade<=60:
    print("retake exam")
else:
    print("input error")
