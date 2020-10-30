import numpy as np
input = np.loadtxt("/Users/rasmuser/Dropbox/ProjectEuler/81matrix.txt", dtype='i', delimiter=',')

n, m = len(input[:,0]), len(input[0,:]) 
cost = [input[i,-1] for i in range(n)]

for i in range(m-2, -1, -1):
    cost[0] = cost[0] + input[0,i]
    for j in range(1, n):
        cost[j] = min(cost[j], cost[j-1]) + input[j,i]
    for j in range(n-2, -1, -1):
        cost[j] = min(cost[j], cost[j+1] + input[j,i])
