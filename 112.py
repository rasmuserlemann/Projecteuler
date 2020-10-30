import numpy as np

def monotonic(x):
    dx = np.diff(x)
    return np.all(dx <= 0) or np.all(dx >= 0)
    
def bouncy(n):
    dig = [int(d) for d in str(n)]
    if not monotonic(dig):
        return 1

S = 1
sum = 0
ratio = 0
prop = 0.99

while ratio < prop:
    if bouncy(S)==1:
        sum = sum + 1
    ratio = sum/S
    S = S+1
    
print(S-1)
    
    