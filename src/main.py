import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data_preprocessing import load_data, preprocess_data
from src.sentiment_analysis import apply_sentiment_analysis
from src.visualization import plot_sentiment

def main():
    # Step 1: Load and preprocess data
    data = load_data('/Users/pranavsharma/Documents/sentiment-analysis-project/data/qualtrics_data.csv')
    data = preprocess_data(data)

    # Step 2: Perform sentiment analysis (score calculation and categorization)
    data = apply_sentiment_analysis(data)

    # Step 3: Visualize results
    plot_sentiment(data, plot_type="histogram")  # Show sentiment score distribution
    plot_sentiment(data, plot_type="pie")        # Show sentiment category distribution

    # Step 4: Save final results
    data.to_csv('data/qualtrics_data_with_sentiment.csv', index=False)
    print("Sentiment analysis completed and results saved to data/qualtrics_data_with_sentiment.csv")

# Run the main function if this file is executed as the main module
if __name__ == "__main__":
    main()