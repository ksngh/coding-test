from collections import deque
import sys

rep = int(sys.stdin.readline())
queue = deque([])
n = 0

for i in range(rep) :
    com = sys.stdin.readline().rstrip()
    if "push" in com :
        n+=1
        if "back" in com :
            queue.append(list(com.split(' '))[1])
        if "front" in com :
            queue.appendleft(list(com.split(' '))[1])
    elif "pop" in com :
        if n == 0 :
            print(-1)
        else :
            n-=1
            if "back" in com:
                print(queue.pop())
            if "front" in com:
                print(queue.popleft())
    elif com == "size" :
        print(n)
    elif com == "empty" :
        if n==0 :
            print(1)
        else :
            print(0)
    elif com == "front" :
        if n==0 :
            print(-1)
        else :
            print(queue[0])
    elif com == "back" :
        if n==0 :
            print(-1)
        else :
            print(queue[-1])