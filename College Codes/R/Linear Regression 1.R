hours = c(2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
marks = c(45, 50, 54, 58, 65, 68, 72, 78, 82, 85)
cor(hours, marks)

data = data.frame(hours, marks)
data
plot(hours, marks, main = "Hours studied VS Marks", xlab = "Hours studied",
     ylab = "Marks obtained", pch = 19, col = "red")

modelYonX = lm(marks~hours)
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


# Regression line for X on Y
modelXonY = lm(hours ~ marks)
summary(modelXonY)
coef(modelXonY)

# Predict marks for 7.5 hours
new_student = data.frame(hours = 7.5)
predict(modelYonX, newdata = new_student)

# Predict hours for a student scoring 75 marks
new_marks = data.frame(marks = 75)
predict(modelXonY, newdata = new_marks)
