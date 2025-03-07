import sys
user_input = sys.stdin.readline().rstrip()
num = int(user_input)

cnt = 0
while True :
    temp_str = str(cnt)
    created_num = cnt
    for i in range(len(temp_str)) :
        created_num += int(temp_str[i])
    if num == created_num :
        print(cnt)
        break
    elif num < cnt :
        print(0)
        break
    cnt += 1