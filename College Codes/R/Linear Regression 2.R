cars
dist = c(cars$dist)
dist
speed = c(cars$speed)
speed
cor(dist, speed)

data = data.frame(speed, dist)
data
plot(speed, dist, main = "Distance covered VS Speed", xlab = "Speed",
     ylab = "Distance", pch = 19, col = "red")

modelYonX = lm(dist~speed)
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

new_speed = data.frame(speed = 20 )
predict(modelYonX, newdata = new_speed)
