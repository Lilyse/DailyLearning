def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n < 1:
        print("输入错误")
        return -1
    while n > 2:
        n3 = n1 + n2 
        n1 = n2
        n2 = n3
        n -= 1
    
    return n3
   
    
result = fab(int(input()))
if result != -1:
    print(result)