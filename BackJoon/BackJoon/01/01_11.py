a = int(input())
b = int(input())

print(a * (b%10))
b1 = b // 10
print(a * (b1%10))
print(a * (b1//10))
print(a * b)