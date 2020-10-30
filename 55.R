library(TeachingDemos)

back = function(x){
  n = length(x)
  sum = 0
  for (m in 1:n){
    sum = sum + x[m]*10^(n-m)
  }
  return(sum)
}

linn = function(x, count){
  dig = digits(x)
  digrev = rev(dig)
  new = x + back(digrev)
  newdig = digits(new)
  newdigrev = rev(newdig)
  if (all.equal(newdig, newdigrev)==TRUE){
    return(1)
  }
  if (count == 50){
    return(0)
  }
  else{
    return(linn(new,count+1))
  }
}

s = 0 

for (k in 1:10000){
  s = s + linn(k, 1)
}