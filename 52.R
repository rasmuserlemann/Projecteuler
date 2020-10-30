for (k in 100000:10000000){
  print(k)
  k1 = digits(k)
  k2 = digits(2*k)
  k3 = digits(3*k)
  k4 = digits(4*k)
  k5 = digits(5*k)
  k6 = digits(6*k)
  if (setequal(k1,k2) & setequal(k2,k3) & setequal(k3,k4) & setequal(k4,k5) & setequal(k5,k6)){
    break
  }
}