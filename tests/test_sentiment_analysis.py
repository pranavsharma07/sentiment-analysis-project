import unittest
import pandas as pd
from src.sentiment_analysis import apply_sentiment_analysis

class TestSentimentAnalysis(unittest.TestCase):

    def test_apply_sentiment_analysis(self):
        data = pd.DataFrame({'Text Response': ['I love this!', 'This is bad.']})
        analyzed_data = apply_sentiment_analysis(data)
        self.assertIn('sentiment_score', analyzed_data.columns)
        self.assertIn('sentiment_category', analyzed_data.columns)
        self.assertEqual(analyzed_data['sentiment_category'][0], 'Positive')
        self.assertEqual(analyzed_data['sentiment_category'][1], 'Negative')

if __name__ == '__main__':
    unittest.main()