N = int(input())

numbers = list(map(int, input().split()))
ormack = []

if numbers[1] > numbers[0]:
        ormack.append(numbers[1] - numbers[0])
else:
    for i in range(2,N):
        if numbers[i-1] < numbers[i]:
            ormack.append(max(numbers[i]-numbers[i-1],numbers[i-1]-numbers[i-2]))        

if len(ormack) == 0:
    print(0)
else:
    print(max(ormack))
