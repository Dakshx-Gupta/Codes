population = c(45, 52, 61, 68, 72, 55, 80, 76, 63, 59, 88, 91, 47, 70, 65)
cat("Population:\n")
print(population)
set.seed(123)

# sample of size 6 with replacement
sample_with = sample(population, size = 6, replace = TRUE)
cat("\nSample with replacement:\n")
print(sample_with)

# sample of size 6 without replacement
sample_without = sample(population, size = 6, replace = FALSE)
cat("\n Sample without replacement:\n")
print(sample_without)

cat("\nMean with replacement: ", mean(sample_with), "\n")
cat("\n Mean without replacement: ", mean(sample_without), "\n")
