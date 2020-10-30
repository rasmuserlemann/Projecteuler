library(Rdice)

CH = function(){
  n = sample(1:16,1)
  if (n==1){
    return(0)
  }
  if (n==2){
    return(10)
  }
  if (n==3){
    return(11)
  }
  if (n==4){
    return(24)
  }
  if (n==5){
    return(39)
  }
  if (n==6){
    return(5)
  }
  if (n==7){
    return(100)
  }
  if (n==8){
    return(100)
  }
  if (n==9){
    return(101)
  }
  if (n==10){
    return(102)
  }
  if (n>10){
    return(103)
  }
}
CC = function(P){
  n = sample(1:16,1)
  if (n==1){
    return(0)
  }
  if (n==2){
    return(10)
  }
  if (n>2){
    return(P)
  }
}

S = 1000000
P = 0
frec = c()
three = 0

for (k in 1:S){
  D1 = sample(1:4,1)
  D2 = sample(1:4,1)
  if (D1==D2){
    three = three + 1
  }
  if (three == 3){
    P = 10
    freq = c(freq,P)
    three = 0
    next
  }
  P = (P + D1+D2)%%40
  
  if (P==2 | P==17 | P==33){
    P = CC(P)
  }
  if (P==7){
    val = CH()
    if (val==100){
      P = 15
    }
    if (val==101){
      P = 12
    }
    if (val==102){
      P = 4
    }
    if (val==103){
      P = 7
    }
    if (val<100){
      P = val
    }
  }
  if (P==22){
    val = CH()
    if (val==100){
      P = 25
    }
    if (val==101){
      P = 28
    }
    if (val==102){
      P = 19
    }
    if (val==103){
      P = 22
    }
    if (val<100){
      P = val
    }
  }
  if (P==36){
    val = CH()
    if (val==100){
      P = 5
    }
    if (val==101){
      P = 12
    }
    if (val==102){
      P = 33
    }
    if (val==103){
      P = 36
    }
    if (val<100){
      P = val
    }
  }
  if (P==30){
    P = 10
  }
  freq = c(freq,P)
}
sort(table(freq))
