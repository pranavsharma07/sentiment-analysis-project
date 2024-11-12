import unittest
import pandas as pd
from src.data_preprocessing import load_data, preprocess_data

class TestDataPreprocessing(unittest.TestCase):

    def test_load_data(self):
        data = load_data('data/qualtrics_data.csv')
        self.assertIsInstance(data, pd.DataFrame)
    
    def test_preprocess_data(self):
        data = pd.DataFrame({'Text Response': ['Hello', 'Hello', None, 'Goodbye']})
        processed_data = preprocess_data(data)
        self.assertEqual(processed_data.shape[0], 2)  # Should remove duplicates and None

if __name__ == '__main__':
    unittest.main()