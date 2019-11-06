import yaml
import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


config = yaml.load(open('../config.yaml'))

df = pd.read_csv(config['absolute_path']+config['csv_path'])

train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

df_copy = train_set.copy()

df_copy.plot.scatter(x='day', y='memory')

test_set_full = test_set.copy()
test_set = test_set.drop(["memory"], axis=1)
test_set.head()

train_labels = train_set["memory"]
train_labels.head()

train_set_full = train_set.copy()
train_set = train_set.drop(["memory"], axis=1)
train_set.head()


lin_reg = LinearRegression()

lin_reg.fit(train_set, train_labels)

with open(config['absolute_path']+config['model_path'], "wb") as file_handler:
  pickle.dump(lin_reg, file_handler)

with open(config['absolute_path']+config['training_data_path'], "wb") as file_handler:
  pickle.dump(train_set, file_handler)

with open(config['absolute_path']+config['training_labels_path'], "wb") as file_handler:
  pickle.dump(train_labels, file_handler)

accuration = lin_reg.score(test_set, test_set_full["memory"])
result = {
  "coefficients": lin_reg.coef_, 
  "intercept": lin_reg.intercept_,
  "accuration": accuration,
}

with open(config['absolute_path']+config['summary_result_path'], "wb") as file_handler:
  pickle.dump(train_labels, file_handler)

print("Coefficients: ", lin_reg.coef_)
print("Intercept: ", lin_reg.intercept_)
print("Accuration: ", accuration)
memory_pred = lin_reg.predict(test_set)
print(memory_pred)
print(lin_reg.predict([[200]]))