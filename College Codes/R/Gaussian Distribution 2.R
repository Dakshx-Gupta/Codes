m = 65
s = 8
z = (81-m)/s
z
pnorm(69, mean = m, s) # P(x < 70)
1-pnorm(71, mean = m, sd = s) # P(x > 70)
pnorm(61:74, mean = m, s) # P(60 < x < 75)
