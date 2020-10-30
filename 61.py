def tri(n):
    result = []
    for i in range(n):
        num = int(i*(i+1)/2)
        if len(str(num))==4:
            result.append(int(num))
        if len(str(num))==5:
            return result
triangle = tri(500)

def squ(n):
    down = int(sqrt(int(n
    up = 
    result = []
    for i in range(n):
        num = int(i**2)
        if len(str(num))==4:
            result.append(int(num))
        if len(str(num))==5:
            return result
square = squ(101)

def pen(n):
    result = []
    for i in range(n):
        num = int(i*(3*i-1)/2)
        if len(str(num))==4:
            result.append(int(num))
        if len(str(num))==5:
            return result
pentagonal = pen(100)

def hex(n):
    result = []
    for i in range(n):
        num = int(i*(2*i-1))
        if len(str(num))==4:
            result.append(int(num))
        if len(str(num))==5:
            return result
hexagonal = hex(100)

def hep(n):
    result = []
    for i in range(n):
        num = int(i*(5*i-3)/2)
        if len(str(num))==4:
            result.append(int(num))
        if len(str(num))==5:
            return result
heptagonal = hep(100)

def oct(n):
    result = []
    for i in range(n):
        num = int(i*(3*i-2))
        if len(str(num))==4:
            result.append(int(num))
        if len(str(num))==5:
            return result
octagonal = oct(100)

