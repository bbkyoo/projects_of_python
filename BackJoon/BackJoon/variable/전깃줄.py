n = int(input())

electronic = []
 
for i in range(n):
    x, y = map(int, input().split())
    electronic.append([x,y])

electronic = sorted(electronic, key = lambda x : x[0])

dp = [0] * n
dp[0] = 1

for i in range(1,n):
    min_value = 0
    for j in range(i):
        if(electronic[i][1] > electronic[j][1]):
            min_value = max(dp[j], min_value)
    dp[i] = min_value + 1
print(n - max(dp))




#dp = []
#electronic_st = sorted(electronic)
#for i in range(n):
#    for j in range(i,n):
#        if electronic_st[i][1] > electronic_st[j][1]:
#            dp.append(electronic_st[i])

#for i in range(n,0,-1):
#    for j in range(i,0):
#        if electronic_st[i][1] < electronic_st[j][1]:
#            dp.append(electronic_st[i])

#result = []
#for i in dp:
#    if i not in result:
#        result.append(i)

#print(len(result))

 