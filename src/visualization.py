import matplotlib.pyplot as plt
import seaborn as sns

def plot_sentiment(data, plot_type="histogram"):
    """
    Plot sentiment analysis results.
    
    Parameters:
    - data: DataFrame containing the sentiment scores and categories
    - plot_type: str, either "histogram" for sentiment score distribution 
                 or "pie" for sentiment category distribution
    """
    if plot_type == "histogram":
        # Plot a histogram of sentiment scores
        plt.figure(figsize=(10, 6))
        sns.histplot(data['sentiment_score'], bins=20, kde=True)
        plt.title('Distribution of Sentiment Scores')
        plt.xlabel('Sentiment Score')
        plt.ylabel('Frequency')
        plt.show()
        
    elif plot_type == "pie":
        # Plot a pie chart of sentiment categories
        sentiment_counts = data['sentiment_category'].value_counts()
        plt.figure(figsize=(8, 6))
        sentiment_counts.plot.pie(autopct='%1.1f%%', startangle=140)
        plt.title('Sentiment Category Distribution')
        plt.ylabel('')
        plt.show()
        
    else:
        print("Invalid plot type. Choose 'histogram' or 'pie'.")