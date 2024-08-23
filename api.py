class API:

    def Sentiment_Analysis(self, text):

        import nltk
        nltk.download('vader_lexicon')
        from nltk.sentiment import SentimentIntensityAnalyzer

        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(text)

        return sentiment_scores

    
    def Language_Detection(self, text):
        
        from langdetect import detect

        language = detect(text)
        return language
    
    
    def NER(self, text):

        import spacy

        # Load the pre-trained model
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        d = {}

        # Extract entities
        for ent in doc.ents:
            d[ent.text] = ent.label_
        
        return d




