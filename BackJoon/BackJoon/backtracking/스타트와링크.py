from itertools import combinations

N = int(input())

S = []

possible_team = []

for i in range(N):
    S.append(list(map(int, input().split())))

num_list = [i for i in range(N)]
res = float('inf') # 양의 무한대

def solve():
    global res
    
    for cand in combinations(num_list, N//2):
        start_member = list(cand)
        link_member = list(set(num_list) - set(cand))

        start_comb = list(combinations(start_member, 2))
        link_comb = list(combinations(link_member, 2))
    
        start_sum = 0
        for x, y in start_comb:
            start_sum += (S[x][y] + S[y][x])

        link_sum = 0
        for x, y in link_comb:
            link_sum += (S[x][y] + S[y][x])

        if (res > abs(start_sum - link_sum)):
            res = abs(start_sum - link_sum)

solve()
print(res)