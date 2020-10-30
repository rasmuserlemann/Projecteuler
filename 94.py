count = 0
lim = 50
eps = 0.00001

for x1 in range(lim+1):
 print(x1)
 for y1 in range(lim+1):
  for x2 in range(lim+1):
   for y2 in range(lim+1):
    side1 = (x1**2+y1**2)**(1/2)
    side2 = (x2**2+y2**2)**(1/2)
    side3 = ((x1-x2)**2+(y1-y2)**2)**(1/2)
    k = sorted([side1, side2, side3])
    if k[0]+k[1]>k[2]-eps and k[0]+k[1]<k[2]+eps:
     continue
    if k[0]**2+k[1]**2>k[2]**2-eps and k[0]**2+k[1]**2<k[2]**2+eps:
     count = count + 1
     print(x1)
     print(x2)
     print(y1)
     print(y2)
     print("...")