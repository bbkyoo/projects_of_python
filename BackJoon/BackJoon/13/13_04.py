#import sys

## 산술 평균 구하기
#def lst_avg(lst):
#    return round(sum(lst) / len(lst))

## 중앙값 구하기
#def lst_median(lst):
#    return lst[(n // 2)]

## 최빈값 구하기 
#def lst_mode(lst):
#    lst_cnt = [0] * n

#    for i in range(n):
#        for j in range(i+1, n):
#            if lst[i] == lst[j]:
#                lst_cnt[i] += 1
    
#    lst_idx = []
    
#    for i in range(n):
#        if lst_cnt[i] == max(lst_cnt):
#            lst_idx.append(i)
    
#    result = []
#    if len(lst_idx) == 1:
#        result.append(lst[lst_idx[0]])
#    else:
#        result.append(lst[lst_idx[1]])
#    return result[0]

## 범위 구하기
#def lst_range(lst):
#    return (max(lst) - min(lst))


#n = int(sys.stdin.readline())

#lst = []

#for _ in range(n):
#    lst.append(int(sys.stdin.readline())) 
#lst.sort()

#print(lst_avg(lst))
#print(lst_median(lst))
#print(lst_mode(lst))
#print(lst_range(lst))