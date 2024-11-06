import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import GradientBoostingRegressor
import joblib

data = pd.read_csv('house_data.csv')
data = data[data.sqft != 0]
# emphasize features
data['sqft'] *= 10
data['baths-squared'] = data['baths'] ** 2
data['beds-squared'] = data['beds'] ** 2

# MACHINE LEARNING STUFF
X = data.drop('price', axis=1)
X = pd.get_dummies(X, columns=['zipCode'])
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.2, max_depth=3, min_samples_split=4, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
scores = cross_val_score(model, X_train, y_train, cv=5, scoring='neg_mean_absolute_error')
print("Average MAE:", -scores.mean())

joblib.dump(model, '../backend/model/model.pkl')