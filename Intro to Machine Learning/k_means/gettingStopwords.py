from nltk.corpus import stopwords

# try retrieve stopwords, else download the package with the words
try:
	sw = stopwords.words("english")
except Exception:
	import nltk
	nltk.download()