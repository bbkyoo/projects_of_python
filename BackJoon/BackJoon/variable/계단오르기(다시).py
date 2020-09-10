# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 
# 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.

n = int(input())

step = list(int(input().strip()) for __ in range(n))

def solve(step, n):
    dp = []
    dp.append(step[0])
    for i in range(1, 3):
        if i == 1:
            dp.append( max(dp[i-1] + step[i], step[i] ))
            continue
        dp.append(max(dp[i-2] + step[i], step[i-1] + step[i]))

    for i in range(3, n):
        dp.append(max(step[i] + step[i-1] + dp[i-3], step[i] + dp[i-2]))

    print(dp[-1])

solve(step, n)




#k = n - 3
#while True:
#    if k <= 0:
#        sum += step[0]
#        break

#    if step[n-2] > step[n-3]:
#        sum = sum + step[n-2] 
#        k -= -1
#    else:
#        if step[k] > step[k-1]:
#            sum += step[k]
#            k -= 1
#        else:
#            sum += step[k-1]
#            k -= 2

    



























