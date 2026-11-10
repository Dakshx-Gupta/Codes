x = c(10, 4, 45, 33, 21, 21, 22, 90, 56, 34)

mean(x)
median(x)
Mode(x)
min(x)
max(x)
range(x)
diff(range(x))
sd(x)
Var(x)

hist(x, col = "skyblue")
barplot(x, names.arg = , main = "Bar", xlab = "Marks", ylab = "Freq")
pie(x, labels = c("GG", "dd", "ff"))
s = skewness(x)
s
k = kurtosis(x)
k
