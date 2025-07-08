import pandas as pd

def transform_to_DataFrame(data):
    """
    Mengonversi list of dict hasil scraping ke DataFrame pandas.
    """
    try:
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        print(f"Gagal mengonversi ke DataFrame: {e}")
        return pd.DataFrame()  # kembalikan DataFrame kosong jika gagal

def transform_data(df, conversion_rate=16000):
    """
    Menghapus simbol $ dari harga dan mengonversi ke float, lalu ke IDR.
    """
    try:
        # Hapus simbol dolar dan konversi ke float
        df['Price'] = df['Price'].replace('[\$,]', '', regex=True).astype(float)
        df['Price'] = df['Price'] * conversion_rate
    except Exception as e:
        print(f"Gagal mengonversi harga ke IDR: {e}")
        df['Price'] = None
    return df
