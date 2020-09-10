N = int(input())

onepan = [ i for i in range(1,N+1)]
treepan = [sum(onepan),0,0]

for i in range(N):
    for j in range(i+1,N):
        if 