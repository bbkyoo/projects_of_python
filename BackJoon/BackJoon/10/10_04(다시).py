def isPrime(num):
    if num == 1:
        return False     
    else:
        for j in range(2,int(num**0.5)+1):
            if num % j == 0:
                return False
    return True

li = list(range(2,246912))
prime_li = []
for i in li:
    if isPrime(i):
        prime_li.append(i)

while True:
    n = int(input())
    count = 0
    if n == 0:
        break
    else:
        for i in prime_li:
            if n< i <= n*2:
                count += 1
    print(count)