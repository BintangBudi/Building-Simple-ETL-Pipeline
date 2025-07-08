import unittest
import os
import pandas as pd
from utils.load import store_to_csv

class TestLoad(unittest.TestCase):
    def test_store_to_csv(self):
        df = pd.DataFrame([{'Title': 'Item A', 'Price': 1600000.0, 'Rating': 4.0, 'Colors': 3, 'Size': 'M', 'Gender': 'Men'}])
        test_file = 'test_output.csv'
        store_to_csv(df, file_path=test_file)
        self.assertTrue(os.path.exists(test_file))
        os.remove(test_file)  # bersihkan file setelah tes

if __name__ == '__main__':
    unittest.main()
