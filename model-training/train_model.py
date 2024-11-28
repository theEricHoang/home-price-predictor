import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import joblib

data = pd.read_csv('clean_house_data.csv')
data = data[data.sqft != 0]

# MACHINE LEARNING STUFF
encoder = ColumnTransformer(
    transformers=[
        ('zipCode', OneHotEncoder(handle_unknown='ignore'), ['zipCode'])
    ],
    remainder='passthrough'
)

pipeline = Pipeline(steps=[
    ('preprocessor', encoder),
    ('model', GradientBoostingRegressor(n_estimators=380, learning_rate=0.2, max_depth=9, min_samples_split=5, min_samples_leaf=1, max_features='sqrt'))
])

X = data.drop('price', axis=1)
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
scores = cross_val_score(pipeline, X_train, y_train, cv=5, scoring='neg_mean_absolute_error')
print("Average MAE:", -scores.mean())

pipeline.fit(X, y)

joblib.dump(pipeline, 'backend/model/model3.joblib')
# CURRENTLY 22% ERROR ON AVERAGE