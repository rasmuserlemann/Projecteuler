import numpy

list = []
c = 0

for ind in range(1, 100001):
    c = c+1
    if c==2:
        list.append(int(ind/2))
        continue
    if c==5:
        list.append(int(ind/5))
        continue
    if c==10:
        list.append(int(ind/10))
        c=0
        continue
    list.append(ind)
        
    