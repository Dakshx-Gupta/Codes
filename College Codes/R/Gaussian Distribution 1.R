x = 70
mu = 60
sigma = 5
z = (x-mu)/sigma
z
pnorm(70, mean = mu, sd = sigma) # P(x <= 70)
1-pnorm(70, mean = mu, sd = sigma) # P(x >= 70)

qnorm(0.95, mean = 60, sd = 10) # (95th Percentile)
qnorm(0.05, mean = 60, sd = 10) # (5th Percentile)

set.seed(123)
marks = rnorm(100, mean = 60, sd = 10)
marks
hist(marks, main = "Simulated Examination Marks", xlab = "Mar")


# Question-1
m = 65
s = 8
z = (81-m)/s
z
pnorm(69, mean = m, s) # P(x < 70)
1-pnorm(71, mean = m, sd = s) # P(x > 70)
pnorm(61:74, mean = m, s) # P(60 < x < 75)
