import sys

rep = int(sys.stdin.readline().rstrip())

temp_li = []

for i in range(rep) :
    temp_li.append(sys.stdin.readline().rstrip())
temp_set = set(temp_li)
result_li = list(temp_set)

result = sorted(result_li,key=lambda x : (len(x),x))

for j in result :
    print(j)