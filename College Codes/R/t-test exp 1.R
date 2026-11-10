marks = c(68, 72, 75, 70, 69, 74, 71, 73, 67, 76)
cat("Sample size: ", length(marks), "/n")
cat("Sample size: ", mean(marks), "/n")
cat("Sample size: ", sd(marks), "/n")
result = t.test(marks, mu = 70, alternative = "two.sided", conf.level = 0.95)
print(result)
if(result$p.value < 0.05){
  cat("Reject HO: the population mean differs from 70\n")
}else{
  cat("Do not reject HO: insufficient evidence that the population mean differs from 70\n")
}
