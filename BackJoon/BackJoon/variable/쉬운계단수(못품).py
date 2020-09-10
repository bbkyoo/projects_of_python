N = int(input())

stair = []
count = 0

for i in range(N):
    stair.append('9'*(i+1))

for i in range(1,int(stair[N-1])):
    if N == 1:
        count = 9
        break
    
