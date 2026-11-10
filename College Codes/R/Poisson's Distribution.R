lambda = 4
dpois(2, lambda)
dpois(5, lambda)
dpois(0, lambda)
ppois(3, lambda) # prob of at most 3 arrivals
1-ppois(3, lambda) # prob more than 3 arrivals
x = 0:10
prob = dpois(x, lambda)
data.frame(x, prob)
barplot(prob, name.arg = x, main = "Poisson's Distribution",
        xlab = "Number of Arrivals", ylab = "Probability")
xpois(100, lambda = 3)
