import sys
from collections import defaultdict

nums,questions = map(int,sys.stdin.readline().rstrip().split(' '))

index_dict = defaultdict(int)
reverse_dict = defaultdict(str)
cnt = 0
for i in range(nums) :
    pokemon = sys.stdin.readline().rstrip()
    cnt += 1
    index_dict[pokemon] += cnt
    reverse_dict[cnt] = pokemon

for k in range(questions) :
    question = sys.stdin.readline().rstrip()
    if question.isdigit() :
        print(reverse_dict[int(question)])
    else :
        print(index_dict[question])


