import sys

rep = int(sys.stdin.readline())
temp_li = []


for i in range(rep) :
    temp_li.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

result = []
for j in range(rep) :
    rank = 1
    for k in range(rep) :
        if temp_li[j][0] < temp_li[k][0] and temp_li[j][1] < temp_li[k][1] :
            rank+=1
    result.append(rank)

print(*result)