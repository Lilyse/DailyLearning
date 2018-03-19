temp = input()
x = int(temp)
a = 1
n = lambda x : x * (x - 1)
while x > 1:
    a = a * n(x)
    x -= 2
print(a)