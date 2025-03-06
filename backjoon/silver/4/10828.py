import sys

a = int(sys.stdin.readline())

stack = []
n = 0
for i in range(a) :
    com = str(sys.stdin.readline().rstrip())

    if com == "pop" :
        if n == 0 :
            print(-1)
        else :
            print(stack.pop())
            n-=1
    elif com == "size" :
        print(n)
    elif com == "empty" :
        if n == 0 :
            print(1)
        else :
            print(0)
    elif com =="top" :
        if n != 0 :
            print(stack[-1])
        else :
            print(-1)
    else :
        temp_li = list(com.split(' '))
        stack.append(temp_li[1])
        n += 1