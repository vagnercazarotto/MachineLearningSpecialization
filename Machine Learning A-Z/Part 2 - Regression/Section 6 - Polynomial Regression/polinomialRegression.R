# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
#library(caTools)
#set.seed(123)
#split = sample.split(dataset$DependentVariable, SplitRatio = 0.8)
#training_set = subset(dataset, split == TRUE)
#test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)

## Fitting Linear Regression to the dataset
lin_reg = lm(formula = Salary ~ .,
             data = dataset) 

summary(lin_reg)

## Fitting Polynomial Regression to the dataset
dataset$Level2 = dataset$Level^2 ## Add a polynomial term
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4
dataset$Level5 = dataset$Level^5
poly_reg = lm(formula = Salary ~ .,
              data = dataset)

summary(poly_reg)


## Visualising the Linearn Regression results
#install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x= dataset$Level , y= dataset$Salary),
             color = 'red') +
  geom_line(aes(x=dataset$Level , y = predict(lin_reg, newdata = dataset)),
            color = 'blue') +
  ggtitle('Truth or Bluf (Linear Regression)') +
  xlab('Level') +
  ylab('Salary')

## Visualising the Polynomial Regression results
#install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x= dataset$Level , y= dataset$Salary),
             color = 'red') +
  geom_line(aes(x=dataset$Level , y = predict(poly_reg, newdata = dataset)),
            color = 'blue') +
  ggtitle('Truth or Bluf (Linear Regression)') +
  xlab('Level') +
  ylab('Salary')


## Predicting a new result with Linear Regression
y_pred = predict(lin_reg, data.frame(Level = 6.5))

## Predicting a new result with a Polynomial Regression
y_poly_pred = predict(poly_reg, data.frame(Level = 6.5, 
                                           Level2 = 6.5^2,
                                           Level3 = 6.5^3,
                                           Level4 = 6.5^4,
                                           Level5 = 6.5^5))
