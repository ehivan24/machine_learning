import numpy as np
from sklearn.naive_bayes import GaussianNB

x = np.array([[-3, 7], [1, 5], [1, 2], [-2, 0], [2, 3],
              [-4, 0], [-1, 1], [1, 1], [-2, 2], [2, 7], [-4, 1], [-2, 7]])
Y = np.array([2, 5, 2, 2, 4, 2, 2, 5, 2, 1, 4, 0])

model = GaussianNB()
model.fit(x, Y)

predicted = model.predict([[1, 2], [5, 4]])
print predicted

