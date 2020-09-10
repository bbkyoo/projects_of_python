def num_sum(a):
    sum = 0
    for i in range(0,len(a),1):
        sum += a[i]
    return sum

n = int(input())
a = []
for j in range(0,n,1):
    a.append(int(input()))

print(num_sum(a))

