def Jiecheng(n):
    if n == 1 :
        return 1
    else:
        return n * Jiecheng(n-1)

number = int(input())
result = Jiecheng(number)
print(result)