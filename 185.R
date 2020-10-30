start = sample(0:9, size = 5, replace = TRUE)

res = matrix(c(9,0,3,4,2,7,0,7,9,4,3,9,4,5,8,3,4,1,0,9,5,1,5,4,5,1,2,5,3,1), nrow = 6, ncol = 5, byrow = TRUE)
corrects = c(2, 0, 2, 1, 2, 1)

check = function(x){
  score = 0
  pos = matrix()
  neg = matrix()
  for (k in 1:length(res[,1])){
    for (kk in 1:length(res[1,])){
      if (res[k,kk]==x[kk] &){
        
        
      }
    }
  }
  return(score)
}