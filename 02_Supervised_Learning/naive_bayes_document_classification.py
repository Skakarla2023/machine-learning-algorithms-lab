import sklearn

docs = ["python coding data",
        "machine learning python",
        "football match goal",
        "team wins cricket"]

labels = ["Tech", "Tech", "Sports", "Sports"]

vec = CountVectorizer()
X = vec.fit_transform(docs)

model = MultinomialNB()
model.fit(X, labels)

test_docs = ["python and data", "watch football match"]
X_test = vec.transform(test_docs)

pred = model.predict(X_test)

for d, p in zip(test_docs, pred):
    print(f"Document: '{d}' → Predicted Category: {p}")
