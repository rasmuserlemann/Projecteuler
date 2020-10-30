def back(x):
    sum = 0
    for i in range(0,len(x)):
        sum = sum + x[i]*10**(len(x)-i-1)
    return(sum)

def linn(x, count):
    num = [int(d) for d in str(x)]
    numrev = num[::-1]
    numrev1 = back(numrev)
    new = numrev1 + x
    num2 = [int(d) for d in str(new)]
    num2rev = num2[::-1]
    if num2 == num2rev:
        return(1)
    if count == 50:
        return(0)
    else:
        return(linn(new, count + 1))

total = 0
for k in range(1,10001):
    total = total + linn(k, 0)