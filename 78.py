nums = range(1,target)

L, target = 5000, 11
while True:
    ways = [1] + [0]*target
    for p in nums:
        for i in range(p, target+1):
            ways[i] += ways[i-p]
    if ways[target] > L: break    
    target += 1

