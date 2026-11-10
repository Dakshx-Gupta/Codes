trees
girth = c(trees$Girth)
girth
volume = c(trees$Volume)
volume
cor(girth, volume)

data = data.frame(volume, girth)
data
plot(girth, volume, main = "Girth VS Volume", xlab = "Girth",
     ylab = "Volume", pch = 19, col = "red")

modelYonX = lm(volume~girth)
summary(modelYonX)
coef(modelYonX)
abline(modelYonX, col = "blue")
fitted.values(modelYonX)
residuals(modelYonX)
data$fitted = fitted(modelYonX)
data$residual = residuals(modelYonX)
data

sse = sum(residuals(modelYonX)^2)
sse
mse = mean(residuals(modelYonX)^2)
mse
rmse = sqrt(mse)
rmse

# Residual Plot
plot(fitted(modelYonX), residuals(modelYonX), main = "Residuals VS fitted values",
     xlab = "Fitted values", ylab = "Residuals", pch = 19, abline(h = 0))

new_girth = data.frame(girth = 12 )
predict(modelYonX, newdata = new_girth)
