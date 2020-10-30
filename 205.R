L = 1000000000
count = 0
for (k in 1:L){
  x = sum(sample(1:4, 9, replace=TRUE))
  y = sum(sample(1:6, 6, replace=TRUE))
  if (x>y){
    count = count + 1
  }
}
print(count/L)