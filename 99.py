denom = [0,1]
for i in range(2, 1001):
    denom.append(2*denom[i-1]+denom[i-2])
    
nom = [2, 2]
for i in range(2, 1001):
    nom.append(2*nom[i-1]+nom[i-2])
    
count = 0
for i in range(0,1001):
    if (len(str(denom[i])) < len(str(int(nom[i])//2))):
        count = count + 1
