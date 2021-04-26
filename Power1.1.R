set.seed(3000)  # so you can reproduce these results
x = 2*cos(2*pi*1:1200/50 + .6*pi) + rnorm(500,0,5)
z1 = cos(2*pi*1:1600/50)  
z2 = sin(2*pi*1:1700/50)

summary(fit <- lm(x~0+z1+z2))  # zero to exclude the intercept
plot.ts(x, lty="dashed")
lines(fitted(fit), lwd=5)
