from textblob import TextBlob

def get_sentiment(text):
    """Calculate the sentiment polarity score for a given text."""
    return TextBlob(text).sentiment.polarity

def categorize_sentiment(score):
    """Categorize sentiment based on the polarity score."""
    if score > 0:
        return 'Positive'
    elif score < 0:
        return 'Negative'
    else:
        return 'Neutral'

def apply_sentiment_analysis(data):
    """Apply sentiment analysis and categorization on the data."""
    # Calculate sentiment scores
    data['sentiment_score'] = data['Text Response'].apply(get_sentiment)
    # Categorize sentiments
    data['sentiment_category'] = data['sentiment_score'].apply(categorize_sentiment)
    return data