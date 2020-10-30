import numpy as np
input = np.loadtxt("/Users/rasmuser/Dropbox/ProjectEuler/81matrix.txt", dtype='i', delimiter=',')


for c in range(1,len(input[:,0])):
    input[0,c]=input[0,c]+input[0,c-1]
    input[c,0]=input[c,0]+input[c-1,0]
    

for a in range(1, len(input[:,0])):
    for b in range(1, len(input[0,])):
        input[a,b]=input[a,b]+min(input[a-1,b],input[a,b-1])
print(input[79,79])