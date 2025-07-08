import unittest
from bs4 import BeautifulSoup
from utils.extract import extract_book_data

class TestExtract(unittest.TestCase):
    def test_extract_book_data(self):
        html = '''
        <div class="product-details">
            <h3>T-shirt Example</h3>
            <div class="price-container"><span class="price">$123.45</span></div>
            <div class="product-details">
                <p>Rating: ⭐ 4.5 / 5</p>
                <p>3 Colors</p>
                <p>Size: M</p>
                <p>Gender: Unisex</p>
            </div>
        </div>
        '''
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find('div', class_='product-details')
        result = extract_book_data(div)
        # Hilangkan timestamp agar bisa dibandingkan
        result.pop('Timestamp', None)
        expected = {
            'Title': 'T-shirt Example',
            'Price': '$123.45',
            'Rating': 4.5,
            'Colors': 3,
            'Size': 'M',
            'Gender': 'Unisex'
        }
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
