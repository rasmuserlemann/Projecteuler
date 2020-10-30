file = scan("/Users/rasmuser/Dropbox/ProjectEuler/names.txt", what = "", sep=",")

num = function(x) {utf8ToInt(x) - utf8ToInt("A") + 1L}

final = c()
for (k in 1:length(file)){
  letters = unlist(strsplit(file[k], ""))
  score = 0
  for (kk in 1:length(letters)){
    score = score + num(letters[kk])
  }
  final = append(final, score*k)
}

