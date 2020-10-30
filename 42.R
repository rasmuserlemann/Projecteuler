file = scan("/Users/rasmuser/Dropbox/ProjectEuler/words.txt", what = "", sep=",", na.strings="")
file = sort(file)

triangles = c()
for (kkk in 1:1000){
  triangles = append(triangles, (kkk*(kkk+1))/2)
}

num = function(x) {utf8ToInt(x) - utf8ToInt("A") + 1L}

nums = c()
for (k in 1:length(file)){
  letters = unlist(strsplit(file[k], ""))
  score = 0
  for (kk in 1:length(letters)){
    score = score + num(letters[kk])
  }
  nums = append(nums, score)
}

final = 0
for (m in 1:length(nums)){
  if (nums[m] %in% triangles){
    final = final + 1
  }
}
