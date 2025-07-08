import unittest
import pandas as pd
from utils.transform import transform_to_DataFrame, transform_data

class TestTransform(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
            {'Title': 'Item A', 'Price': '$100.00', 'Rating': 4.0, 'Colors': 3, 'Size': 'M', 'Gender': 'Men'}
        ]

    def test_transform_to_dataframe(self):
        df = transform_to_DataFrame(self.raw_data)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.iloc[0]['Title'], 'Item A')

    def test_transform_data_price_conversion(self):
        df = transform_to_DataFrame(self.raw_data)
        transformed_df = transform_data(df, conversion_rate=16000)
        self.assertAlmostEqual(transformed_df.iloc[0]['Price'], 1600000.0)

if __name__ == '__main__':
    unittest.main()
