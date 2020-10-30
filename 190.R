iterations = 1000

m = 10
init = c(m)
for (kk in 2:m){
  init = append(init, 0)
}

P = function(x){
  value = 1
  for (ind in 1:m){
    value = value*x[ind]^ind
  }
  return(value)
}

for (kkk in 1:iterations){
  init2 = init

  old = P(init)
  init = c(0)
  for (kk in 2:m){
    s = sum(init)
    init = append(init, runif(n=1, min = 0, max = m-s))
  }
  init[0] = m - sum(init)
  
  new = P(init)
  alpha = new/old
  p = runif(1)

  if (new < old && alpha > p){
    init = init2
  }
}
print(old)