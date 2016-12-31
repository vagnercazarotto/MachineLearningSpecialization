import pickle
import numpy as np
from sklearn.preprocessing import MinMaxScaler
data_dict = pickle.load(
    open("../final_project/final_project_dataset.pkl", "r"))
# remove this outlier
data_dict.pop("TOTAL", 0)

salary = []
ex_stock = []

for user in data_dict:
    value = data_dict[user]["salary"]
    if value == "NaN":
        continue
    salary.append(float(value))
    value = data_dict[user]["exercised_stock_options"]
    if value == "NaN":
        continue
    ex_stock.append(float(value))

salary = [min(salary), 200000.0, max(salary)]
ex_stock = [min(ex_stock), 1000000.0, max(ex_stock)]

print "Salary: " + str(salary)
print "Stock : " + str(ex_stock)

salary = np.array([[e] for e in salary])
ex_stock = np.array([[e] for e in ex_stock])

scaler_salary = MinMaxScaler()
scaler_stock = MinMaxScaler()

reescaled_salary = scaler_salary.fit_transform(salary)
reescaled_stock = scaler_stock.fit_transform(ex_stock)

print "Reescaled Salary:" + str(reescaled_salary)
print "Reescaled Stock:" + str(reescaled_stock)

