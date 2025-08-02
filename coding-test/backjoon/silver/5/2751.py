import sys

rep = int(sys.stdin.readline().rstrip())
result = []


for i in range(rep) :
    result.append(int(sys.stdin.readline().rstrip()))

result = sorted(result)
for j in result :
    print(j)