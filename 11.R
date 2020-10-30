T = c()
for (k in 1:1000000){
u1 = runif(1,0,50)
u2 = runif(1,0,40)
u3 = runif(1,0,30)
a = sqrt(30^2+u3^2)
b = sqrt(40^2+u2^2)
c = 50
co = (a^2+b^2-c^2)/(2*a*b)
T = append(T, acos(co)/(2*pi))
}