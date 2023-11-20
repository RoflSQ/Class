n = int(input())
stl = []
for i in range(n):
    k = int(input())
    stl.append(k)
p = int(input())
stl = list(reversed(stl))
tmp = []
new = 1
frst = stl.pop(0)
for d in range(100):
    summ = frst
    new = 1
    for k in stl:
        new += d
        summ += k * new
    if p > summ:
        tmp.append(d)
print(max(tmp))
