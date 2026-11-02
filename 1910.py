#1
n = int(input())
l = []
for i in range(n):
    l.append(i)
print(l)

#2

n = int(input())
l = []
for i in range(n+1):
    l.append(i**2)
print(l)

#3



#4

a = [2,4,5,6,7,2,-1,-2,-3]
s = 1
for i in a:
    s *= i
print(s)

#9

a = [2,4,5,6,7,2,-1,-2,-3]

l = len(a)
for i in range(l):
    if a[i] < 0:
        a[i] = 0
print(a[i])