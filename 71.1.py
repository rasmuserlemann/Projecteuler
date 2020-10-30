limit = 8

def hcf(a,b):
 if(b==0):
  return a
 else:
  return hcf(b,a%b) 
  

for d in range(1,1000000:
 print(d)
 a = 3000000-7*d
 b = 1000000
 h = hcf(a,b)
 aa = a/h
 bb = b/h
 if (aa<1000000 and bb<1000000):
  print(a)
  break