import sys
from collections import deque

rep = int(sys.stdin.readline())
queue = deque([])
n = 0

for i in range(rep) :
    a = sys.stdin.readline().rstrip()
    if a.startswith("push") :
        queue.append(list(a.split(' '))[1])
        n+=1
    elif a == "pop" :
        if n== 0 :
            print(-1)
        else :
            print(queue.popleft())
            n-=1

    elif a == "size" :
        print(n)
    elif a == "empty" :
        if n==0 :
            print(1)
        else :
            print(0)
    elif a == "front" :
        if n == 0 :
            print(-1)
        else :
            print(queue[0])
    elif a == "back" :
        if n == 0 :
            print(-1)
        else :
            print(queue[-1])