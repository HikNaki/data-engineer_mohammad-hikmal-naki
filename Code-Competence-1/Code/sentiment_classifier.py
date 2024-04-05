import pandas as pd

class SentimentClassifier:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.data = None
    
    def load_data(self):
        
        # Load Dataset
        self.data = pd.read_csv(self.dataset_path)
        print("Data berhasil dimuat.")

    def classify_sentiment(self):
        if self.data is None:
            print("Error: Data belum dimuat.")
            return
        
        # Klasifikasi sentimen berdasarkan nilai label
        self.data['sentiment'] = self.data['labels'].apply(lambda x: '1' if x == 'good' else ('2' if x == 'bad' else '3'))
        print("Sentimen berhasil diklasifikasikan.")
        
        group = self.data.groupby('labels')

    def save_to_csv(self):
        if self.data is None:
            print("Error: Data belum dimuat.")
            return
        
        # Pisahkan data berdasarkan sentimen
        good_tweets = self.data[self.data['sentiment'] == '1']
        bad_tweets = self.data[self.data['sentiment'] == '2']
        neutral_tweets = self.data[self.data['sentiment'] == '3']
        
        # Simpan ke file CSV
        good_tweets.to_csv('sentiment_chatgpt/sentiment_good.csv', index=False)
        bad_tweets.to_csv('sentiment_chatgpt/sentiment_bad.csv', index=False)
        neutral_tweets.to_csv('sentiment_chatgpt/sentiment_neutral.csv', index=False)
        
        print("File klasifikasi sentiments berhasil disimpan.")

    def summarize_counts(self):
        if self.data is None:
            print("Error: Data belum dimuat.")
            return
        
        # Hitung jumlah tweets untuk masing-masing sentimen
        sentiment_counts = self.data['sentiment'].value_counts().reset_index()
        sentiment_counts.columns = ['sentiment', 'Count']
        
        # Simpan ke file CSV
        sentiment_counts.to_csv('sentiment_chatgpt/sentiment_counts.csv', index=False)
        
        print("File sentiment_counts.csv berhasil disimpan.")



classifier = SentimentClassifier("data_source/dataset.csv")
classifier.load_data()
classifier.classify_sentiment()
classifier.save_to_csv()
classifier.summarize_counts()