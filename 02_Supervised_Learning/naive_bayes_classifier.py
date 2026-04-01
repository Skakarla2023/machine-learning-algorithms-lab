from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

print("="*60)
print("Example: Gaussian Naive Bayes Classifier")
print("="*60)

X, y = load_iris(return_X_y = True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print("\nTraining samples :", len(X_train))
print("Test samples :",len(X_test))
print("Accuracy: ",round(acc,4))

print("\nFirst 5 predictions: ",y_pred[:5])
print("Actual test label: ",y_test[:5])

probs = model.predict_proba([X_test[0]])

print("\nprint sample probabilities")
print("class probability:",probs[0])

print("="*60)
