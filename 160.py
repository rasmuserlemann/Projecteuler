import numpy
P1 = [0]*(4*9+1)
P2 = [0]*(6*6+1)
count1 = 0
count2 = 0

for a in range(1,5):
	for b in range(1,5):
		for c in range(1,5):
			for d in range(1,5):
				for e in range(1,5):
					for f in range(1,5):
						for g in range(1,5):
							for h in range(1,5):
								for i in range(1,5):
									v = a+b+c+d+e+f+g+h+i
									P1[v] = P1[v] + 1
									count1 = count1 + 1


for a in range(1,7):
	for b in range(1,7):
		for c in range(1,7):
			for d in range(1,7):
				for e in range(1,7):
					for f in range(1,7):
						v = a+b+c+d+e+f
						P2[v] = P2[v] + 1
						count2 = count2 + 1

p = [0, 0,  0,  1,   9,  45, 165, 486, 1206, 2598, 4950, 8451, 13051, 18351, 23607,\
27876, 30276, 30276, 27876, 23607, 18351, 13051, 8451, 4950, 2598, 1206, 486, 165, 45, 9, 1]

#number of ways of rolling a total of n using 6 six-sided dice (cubic)
c = [1, 6, 21, 56, 126, 252, 456, 756, 1161, 1666, 2247, 2856, 3431, 3906, 4221,\
4332, 4221, 3906, 3431, 2856, 2247, 1666, 1161, 756, 456, 252, 126, 56, 21, 6, 1]
 

w = 0
t = (4**9) * (6**6.)
for C in range(0, 31):
    for P in range (C+1, 31):
        w += p[P]*c[C]
 
print("Project Euler 205 Solution =", round(w/t,7))