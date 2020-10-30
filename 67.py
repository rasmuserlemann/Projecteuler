file = open("/Users/rasmuser/Dropbox/ProjectEuler/base.txt", "r")
base = []
exp = []
for line in file:
    line = line.split(",")
    line[1] = line[1].strip("\n")
    base.append(int(line[0]))
    exp.append(int(line[1]))
    
baselog = []
for k in range(0,len(base)):
    baselog.append(math.log(base[k])*exp[k])