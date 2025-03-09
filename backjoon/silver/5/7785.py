from collections import defaultdict
import sys

rep = int(sys.stdin.readline())
temp_dic = defaultdict(int)

for i in range(rep) :
    name,behavior = sys.stdin.readline().rstrip().split(' ')
    if behavior == "enter":
        temp_dic[name] += 1
    elif behavior == "leave":
        temp_dic[name] -= 1

temp_li = []

for i in temp_dic :
    if temp_dic.get(i)==1:
        temp_li.append(i)

result = sorted(temp_li,reverse=True)
for j in result :
    print(j)