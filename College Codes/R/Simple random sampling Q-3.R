population = c(20, 25, 30, 32, 35, 40, 42, 45, 50, 55)
cat("Population:\n")
print(population)
set.seed(123)

# sample of size 4 with replacement
sample_with = sample(population, size = 4, replace = TRUE)
cat("\nSample with replacement:\n")
print(sample_with)

# sample of size 4 without replacement
sample_without = sample(population, size = 4, replace = FALSE)
cat("\n Sample without replacement:\n")
print(sample_without)

cat("\nMean with replacement: ", mean(sample_with), "\n")
cat("\n Mean without replacement: ", mean(sample_without), "\n")
