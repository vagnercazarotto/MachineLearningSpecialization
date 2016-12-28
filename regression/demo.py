from sklearn import linear_model
regClf = linear_model.LinearRegression()
regClf.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

print regClf.coef_



reg = linear_model.Ridge (alpha = .5)
reg.fit ([[0, 0], [0, 0], [1, 1]], [0, .1, 1]) 


reg.coef_

print reg.intercept_ 




reg = linear_model.LassoLars(alpha=.1)
reg.fit([[0, 0], [1, 1]], [0, 1])  



print reg.coef_   