import math

def is_square(integer):
    root = math.sqrt(integer)
    return integer == int(root + 0.5) ** 2

def CF(n):
 if is_square(n):
  return [int(math.sqrt(n))]
 ans = []
 step1_num = 0
 step1_denom = 1
 while True:
  nextn = int((math.floor(math.sqrt(n)) + step1_num) / step1_denom)
  ans.append(int(nextn))
  step2_num = step1_denom
  step2_denom = step1_num - step1_denom * nextn
  step3_denom = (n - step2_denom ** 2) / step2_num
  step3_num = -step2_denom
  if step3_denom == 1:
   ans.append(ans[0] * 2)
   break
  step1_num, step1_denom = step3_num, step3_denom
 return ans

big = 0

for N in range(3,10):
 if is_square(N):
  continue
 C = CF(N)
 h = [1,C[0]]
 k = [0,1]
 if (h[1]**2-N*k[1]**2 == 1):
  if h[1] > big:
   big = h[1]
   print(N)
  continue
 for ind in range(1, len(C)):
  conv1 = C[ind]*h[ind]+h[ind-1]
  conv2 = C[ind]*k[ind]+k[ind-1]
  h.append(conv1)
  k.append(conv2)
  if (conv1**2-N*conv2**2 == 1):
   if conv1 > big:
    big = conv1
    print(N)
   break

