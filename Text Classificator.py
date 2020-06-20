import pandas as pd

df = pd.read_table('smsspamcollection',
                   sep='\t',
                   header=None,
                   names=['label', 'sms_message'])

#Label emails as either spam or not

df['label'] = df.label.map({'ham':0, 'spam':1})

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df['sms_message'],
                                                    df['label'],
                                                   random_state=1)
#Apply Bag of Words

from sklearn.feature_extraction.text import CountVectorizer

count_vector = CountVectorizer()
training_data = count_vector.fit_transform(X_train)
testing_data = count_vector.transform(X_test)

#Apply Naive Bayes

from sklearn.naive_bayes import MultinomialNB

naive_bayes = MultinomialNB()

MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)

naive_bayes.fit(training_data, y_train)
predictions = naive_bayes.predict(testing_data)

#Evaluation

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

print('Accuracy score: ', accuracy_score(y_test, predictions))
print('Precision score: ', precision_score(y_test, predictions))
print('Recall score: ', recall_score(y_test, predictions))
print('F1 score: ', f1_score(y_test, predictions))
