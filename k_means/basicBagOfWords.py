from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()

string1 = "hi katie the self driving car will be be be late Best Sebastian"
string2 = "hi Sebastian the machine learning class will be great great Best Katie"
string3 = "hi katie the machine learning class will be most excellent"

emailList = [string1,string2,string3]

#first fit the data, then transform the data
bagOfWords = vectorizer.fit(emailList)
bagOfWords = vectorizer.transform(emailList)

print bagOfWords

#what feature number it is?
print vectorizer.vocabulary_.get("great")
