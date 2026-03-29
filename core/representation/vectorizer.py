from sklearn.feature_extraction.text import TfidfVectorizer

class TFIDFVectorizer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def fit_transform(self, documents):
        """
        Fit the TF-IDF model and transform documents
        """
        return self.vectorizer.fit_transform(documents)

    def transform(self, documents):
        """
        Transform new documents using existing model
        """
        return self.vectorizer.transform(documents)