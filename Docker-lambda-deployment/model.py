import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Load the dataset
df = pd.read_csv("https://github.com/bgweber/Twitch/raw/master/Recommendations/games-expand.csv")

# Prepare the features and target variable
x = df.drop(['label'], axis=1)
y = df['label']

# Initialize and train the model
model = LogisticRegression(max_iter=1000)  # Ensure convergence with more iterations if needed
model.fit(x, y)

# Print the model parameters for debugging (optional)
print("Model coefficients:", model.coef_)
print("Model intercept:", model.intercept_)

# Save the model to a file
with open("logit.pkl", 'wb') as f:
    pickle.dump(model, f)

print("Model saved to logit.pkl")

