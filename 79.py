file = open("/Users/rasmuser/Dropbox/ProjectEuler/tri.txt", "r")
triangle = []

for line in file:
    line = line.split(" ")
    line[-1] = line[-1].strip("\n")
    line = list(map(int, line))
    triangle.append(line)

for row in range(len(triangle)-2, -1, -1):
    for element in range(len(triangle[row])):
        triangle[row][element]=triangle[row][element]+max(triangle[row+1][element], triangle[row+1][element+1])
        
    
    
