from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import metrics
categories=['alt.atheism','soc.religion.christian','comp.graphics','sci.med']
X_train=fetch_20newsgroups(subset='train',categories=categories,shuffle=True,random_state=42)
text_clf=Pipeline([('vect',CountVectorizer()),
                   ('tfidf',TfidfTransformer()),
                   ('clf',MultinomialNB())])
text_clf.fit(X_train.data,X_train.target)
X_test=fetch_20newsgroups(subset='test',categories=categories,shuffle=True,random_state=42)
predicted=text_clf.predict(X_test.data)
print(metrics.accuracy_score(predicted,X_test.target))
print(metrics.classification_report(X_test.target,predicted,target_names=X_test.target_names))
print(metrics.confusion_matrix(X_test.target,predicted))