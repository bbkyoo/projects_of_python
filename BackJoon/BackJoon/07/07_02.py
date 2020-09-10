def Han(n):
    cnt = 0
    if n < 100:
        return n
    else:
        for i in range(100,n+1):
            hun = i//100
            ten = (i//10)%10
            one = i % 10
            if hun - ten == ten - one:
                cnt += 1
        
        return 99+cnt    

num = int(input())
print(Han(num))







