#create population dataset
population = 1:20
cat("Population:\n")
print(population)
set.seed(123)
# sample of size 5 with replacement
sample_with = sample(population, size = 5, replace = TRUE)
cat("\nSample with replacement:\n")
print(sample_with)

# sample of size 5 without replacement
sample_without = sample(population, size = 5, replace = FALSE)
cat("\n Sample without replacement:\n")
print(sample_without)

cat("\nMean with replacement: ", mean(sample_with), "\n")
cat("\n Mean without replacement: ", mean(sample_without), "\n")

