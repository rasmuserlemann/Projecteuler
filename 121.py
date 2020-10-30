steps = 15
L = [1]
LR = [0]

for k in range(1,steps+1):
    Ltemp = []
    LRtemp = []
    for v in range(len(L)):
        Ltemp.append(L[v])
        LRtemp.append(LR[v])
        Ltemp.append(k*L[v])
        LRtemp.append(LR[v]+1)
    L = Ltemp
    LR = LRtemp

total = 0
for a in range(len(L)):
    if LR[a]<=steps//2:
        total += L[a]
print(int(sum(L)/total))
