primes = sieve(1000000)
primes2 = primes[primes > 7]

back = function(x){
  sum = 0
  l = length(x)
  for (i in 1:l){
    sum = sum + x[i]*10^(l-i)
  }
  return(sum)
}

V = c()

for (p in primes2){
  dig = digits(p)
  for (k in 1:(length(dig)-1)){
    num1 = dig[1:k]
    num2 = dig[k+1:length(dig)]
    num11 = back(num1)
    num22 = back(num2)
    if (num11 %in% primes == FALSE | num22 %in% primes == FALSE){
      break
    }
    V = append(V, p)
    print(p)
  }
}