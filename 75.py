import numpy as np
input = np.loadtxt("/Users/rasmuser/Dropbox/ProjectEuler/102tri.txt", dtype='i', delimiter=',')

count = 0

for tri in input:
    px = 0
    py = 0
    p0x = tri[0]
    p0y = tri[1]
    p1x = tri[2]
    p1y = tri[3]
    p2x = tri[4]
    p2y = tri[5]
    Area = 0.5*(-p1y*p2x + p0y*(-p1x + p2x) + p0x*(p1y - p2y) + p1x*p2y)
    s = 1/(2*Area)*(p0y*p2x - p0x*p2y + (p2y - p0y)*px + (p0x - p2x)*py)
    t = 1/(2*Area)*(p0x*p1y - p0y*p1x + (p0y - p1y)*px + (p1x - p0x)*py)
    if s>0 and t>0 and 1-s-t>0:
        count = count + 1