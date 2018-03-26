def jiecheng(n):
    result = n
    for i in range(1,n):
        result *= i
        
    return result

number = int(input())
result = jiecheng(number)
print(result)