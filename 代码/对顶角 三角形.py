n=int(input('请输入图形的行数：'))
for i in range(n,0,-1):
    print(''.rjust(20-i),end='')
    for j in range(2*i-1):
        print('*',end='')
    print('\n')
for i in range(1,n):
    print(''.rjust(19-i),end='')
    for j in range(2*i+1):
        print('*',end='')
    print('\n')
