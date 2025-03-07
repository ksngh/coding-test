import sys

num = int(sys.stdin.readline().rstrip())
start = 665
devil = "666"
cnt = 0

while cnt<num :
    start += 1
    if devil in str(start) :
        cnt += 1

print(start)
