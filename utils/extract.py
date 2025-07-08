import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    )
}

import requests

def fetching_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Akan memicu exception jika 404, 500, dll.
        return response.text
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"Halaman tidak ditemukan: {url}")
        else:
            print(f"Terjadi kesalahan ketika melakukan requests terhadap {url}: {e}")
        return None


import re

def extract_book_data(div):
    """Mengambil data produk fashion: judul, harga, rating, jumlah warna, ukuran, dan gender."""

    book_title = div.find('h3').text.strip()

    # Ambil harga
    price_element = div.find('div', class_='price-container')
    price = price_element.find('span', class_='price').text.strip() if price_element else None

    # Ambil elemen detail produk
    details_div = div.find('div', class_='product-details')
    rating = None
    colors = None
    size = None
    gender = None

    for p in div.find_all('p'):
            text = p.get_text(strip=True)

            if "Rating" in text:
                match = re.search(r'⭐\s*([\d.]+)\s*/\s*5', text)
                rating = float(match.group(1)) if match else None
            elif "Colors" in text:
                match = re.search(r'(\d+)\s+Colors', text)
                colors = int(match.group(1)) if match else None
            elif "Size:" in text:
                match = re.search(r'Size:\s*(\w+)', text)
                size = match.group(1) if match else None
            elif "Gender:" in text:
                match = re.search(r'Gender:\s*(\w+)', text)
                gender = match.group(1) if match else None

    books = {
        "Title": book_title,
        "Price": price,
        "Rating": rating,
        "Colors": colors,
        "Size": size,
        "Gender": gender,
         "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return books


def scrape_book(base_url, delay=2):
    """Mengambil data dari semua halaman katalog fashion."""
    data = []
    page_number = 1

    while True:
        if page_number == 1:
            url = base_url  # halaman pertama tanpa "page" di URL
        else:
            url = f"{base_url}page{page_number}"

        print(f"Scraping halaman: {url}")
        content = fetching_content(url)
        if content:
            soup = BeautifulSoup(content, "html.parser")
            products = soup.find_all('div', class_='product-details')

            if not products:
                print("Tidak ada produk ditemukan, berhenti.")
                break

            for product in products:
                item = extract_book_data(product)
                data.append(item)

            page_number += 1
            time.sleep(delay)
        else:
            print("Gagal mengambil konten halaman.")
            break

    return data


