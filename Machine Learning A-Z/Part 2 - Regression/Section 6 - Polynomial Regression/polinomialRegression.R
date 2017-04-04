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