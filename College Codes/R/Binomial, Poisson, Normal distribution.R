set.seed(123)
binomial_data = rbinom(1000, size = 10, prob = 0.7)
poisson_data = rpois(1000, lambda = 4)
normal_data = rnorm(1000, mean = 60, sd = 10)
barplot(table(binomial_data), main = "Simulated Binomial Distribution", 
        xlab = "Number of Successes", ylab = "Frequency")
barplot(table(poisson_data), main = "Simulated Poisson Distribution",
        xlab = "Number of events", ylab = "Frequency")
hist(normal_data, probability = TRUE, main = "Simulated Normal Distribution",
     xlab = "Value")
lines(density(normal_data), col = "blue", lwd = 2)
comparison = data.frame(Distribution = c("Binomial", "Poisson", "Normal"),
                        Mean = c(mean(binomial_data), mean(poisson_data),
                                 mean(normal_data)),
                        SD = c(sd(binomial_data), sd(poisson_data), sd(normal_data)))
comparison
