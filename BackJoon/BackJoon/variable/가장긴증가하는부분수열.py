#N = int(input())

#A = list(map(int, input().split()))

#dp = []
#dp.append(A[0])

#if N > 1:
#    dp.append(A[1])
#    i = 2
#    while True:
#        for j in range(2,N):
#            if dp[i-1] > dp[i-2] and A[j] > dp[i-1]:
#                dp.append(A[j])
#                break
#            elif A[j] > dp[i-2] and dp[i-1] < dp[i-2]:
#                dp.append(A[j])
#                break

#        if i == len(dp):
#            break
#        i += 1

#if len(A) > 1 and dp[0] > dp[1]:
#    dp.remove(dp[1])

#print(len(dp))

n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))