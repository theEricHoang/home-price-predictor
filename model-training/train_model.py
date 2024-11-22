import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import GradientBoostingRegressor
import joblib

data = pd.read_csv('clean_house_data.csv')
data = data[data.sqft != 0]

# MACHINE LEARNING STUFF
X = data.drop('price', axis=1)
X = pd.get_dummies(X, columns=['zipCode'])
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = GradientBoostingRegressor(n_estimators=380, learning_rate=0.2, max_depth=9, min_samples_split=5, min_samples_leaf=1, max_features='sqrt', random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
scores = cross_val_score(model, X_train, y_train, cv=5, scoring='neg_mean_absolute_error')
print("Average MAE:", -scores.mean())

joblib.dump(model, 'model2.pkl')
# CURRENTLY 22% ERROR ON AVERAGE