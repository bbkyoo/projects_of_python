N = int(input())
count = 0
minimum = [N]

def cal(N):
    list = []
    for i in N:
        list.append(i-1)
        if i%3 == 0:
            list.append(i/3)
        if i%2 == 0:
            list.append(i/2)
    return list

while True:
    if N == 1:
        break
    
    temp = minimum
    minimum = cal(temp)
    count += 1

    if min(minimum) == 1:
        break
    
print(count)