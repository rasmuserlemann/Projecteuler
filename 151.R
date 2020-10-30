options(digits=7)
times = c()
cut = function(x, a){
  if (x == 4){
    a[4] = a[4]-1
    return(a)
  }
  else{
    a[x] = a[x]-1
    a[x+1] = a[x+1]+2
    return(cut(x+1, a))
  }
}

for (k in 1:1000000){
count = -1
a = c(1,1,1,1)

for (k in 1:14){
  b = c(rep(1, a[1]), rep(2, a[2]), rep(3, a[3]), rep(4, a[4]))
  if (length(b) == 1){
    x = b
  }
  else{
    x = sample(b, 1) 
  }
  a = cut(x, a)
  if (sum(a) == 1){
    count = count + 1
  }
}

times = append(times, count)
}
print(sum(times)/length(times))
