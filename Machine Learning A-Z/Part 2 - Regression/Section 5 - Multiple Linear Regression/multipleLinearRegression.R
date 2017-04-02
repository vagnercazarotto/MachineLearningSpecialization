# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('50-Startups.csv')

# we need to resolv Dummy data
# Encoding categorical data
dataset$State = factor(dataset$State,
                         levels = c('New York', 'California'),
                         labels = c(1, 2))


# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)


## Fitting Multiple Linear Regression to the Training set
## dot represent all the linear combinations
regressor = lm(formula = Profit ~ .,
               data = training_set) 

# get information about our regressor
summary(regressor)


## Predict the Test set Results
y_pred = predict(regressor , newdata = test_set)
