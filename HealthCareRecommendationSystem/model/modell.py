import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Preprocess the data
def preprocess_data(data):
    # Handle missing values
    data.fillna(method='ffill', inplace=True)
    
    # Feature Engineering: Calculate BMI
    data['BMI'] = data['weight'] / (data['height'] ** 2)
    
    # Return features and target
    X = data[['age', 'BMI', 'exercise_level']]  # Adjust based on your dataset
    y = data['health_recommendation']  # Adjust based on your dataset
    return X, y

# Train the model
def train_model(X_train, y_train):
    rf_model = RandomForestClassifier()

    # Hyperparameter tuning using GridSearchCV
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }

    grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid,
                               scoring='accuracy', cv=3, verbose=2, n_jobs=-1)

    # Fit the model
    grid_search.fit(X_train, y_train)

    return grid_search.best_estimator_

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

# Save the trained model
def save_model(model, filename):
    joblib.dump(model, filename)

if __name__ == "__main__":
    # Load data
    data = load_data('data/health_data.csv')  # Adjust the path as needed
    X, y = preprocess_data(data)

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    best_model = train_model(X_train, y_train)

    # Evaluate the model
    evaluate_model(best_model, X_test, y_test)

    # Save the trained model
    save_model(best_model, 'model/health_model.pkl')
