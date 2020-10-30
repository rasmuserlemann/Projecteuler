m = 10
init = [0 for x in range(0,m)]
init[0] = m

init2 = init

def P(x):
 value = 1
 for ind in range(0,len(x)):
  value = value*x[ind]**ind
 return value
  

old = P(init)
init = [0 for x in range(0,m)]
for k in range(0,m):
 s = sum(init)
 init[k] = unif(0,s)

new = P(init)
alpha = new/old
p = unif(0,1)

if new < old and alpha < p:
 init = init2
 
 
 

 
