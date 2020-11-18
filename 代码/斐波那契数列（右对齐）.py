a,b=0,1
for i in range(1,21):
    a,b = b,a+b#一一相对应
    print('{0:6d}'.format(a),end=" ")#左补齐，留空位
    if i % 4==0:
        print()#打印空行
