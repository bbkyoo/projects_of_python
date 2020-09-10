N = int(input())
mini = [N]
count = 0

def solve(temp):
    lt = []

    for i in temp:
        lt.append(i-1)
        if i % 3 == 0:
            lt.append(i/3)
        if i % 2 == 0:
            lt.append(i/2)

    return lt


while True:
    if N == 1:
        break
    
    temp = mini
    mini = solve(temp)
    count += 1

    if min(mini) == 1:
        break

print(count)