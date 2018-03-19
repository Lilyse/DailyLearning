def Jiecheng(x):
    x *= (x-1)
    return x
temp = int(input())
x = int(temp)
n = 1
while x > 1 :
    a = Jiecheng(x)
    n = n * a
    x -= 2
print(n)