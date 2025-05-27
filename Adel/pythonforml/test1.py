import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

# Load the diabetes dataset

# dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])


diabetes = datasets.load_diabetes()
diabetes_X = np.array([[1], [2], [3]])
# Use only one feature to tarin the model
diabetes_X_train = diabetes_X
# Use only one feature to test the model
diabetes_X_test = diabetes_X
# Use only one labels to train the model
diabetes_y_train = np.array([3, 2, 4])
# Use only one labels to test the model
diabetes_y_test = np.array([3, 2, 4])

# Create linear regression object
model=linear_model.LinearRegression()
# Train the model using the training sets
model.fit(diabetes_X_train, diabetes_y_train)
# The coefficients
diabetes_y_test_pred = model.predict(diabetes_X_test)

plt.scatter(diabetes_X_test, diabetes_y_test)
plt.plot(diabetes_X_test, diabetes_y_test_pred)
plt.show()

print("Mean squared error is: ", mean_squared_error(diabetes_y_test, diabetes_y_test_pred))
print("Weights: ", model.coef_)
print("Intercept: ", model.intercept_)


