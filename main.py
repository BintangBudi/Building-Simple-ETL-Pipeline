import os
from dotenv import load_dotenv
from utils.extract import scrape_book
from utils.transform import transform_data, transform_to_DataFrame
from utils.load import store_to_csv
from utils.load import append_df_to_google_sheets, store_to_postgresql

# Load environment variables from .env file
load_dotenv()

def main():
    BASE_URL = 'https://fashion-studio.dicoding.dev/'
    all_books_data = scrape_book(BASE_URL)

    if all_books_data:
        try:
            df = transform_to_DataFrame(all_books_data)
            df = transform_data(df, 20000)
            df.drop_duplicates(inplace=True)
            df.dropna(inplace=True)

            # Store in CSV
            store_to_csv(df, 'submission_data.csv')

            # --- MODIFICATION FOR GOOGLE SHEETS ---
            # 1. Build the credentials dictionary from environment variables
            credentials = {
                "type": os.getenv("TYPE"),
                "project_id": os.getenv("PROJECT_ID"),
                "private_key_id": os.getenv("PRIVATE_KEY_ID"),
                "private_key": os.getenv("PRIVATE_KEY").replace('\\n', '\n'),
                "client_email": os.getenv("CLIENT_EMAIL"),
                "client_id": os.getenv("CLIENT_ID"),
                "auth_uri": os.getenv("AUTH_URI"),
                "token_uri": os.getenv("TOKEN_URI"),
                "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
                "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
                "universe_domain": os.getenv("UNIVERSE_DOMAIN"),
            }

            # 2. Pass the credentials dictionary instead of the filename
            append_df_to_google_sheets(
                df,
                spreadsheet_id='1jdapyvdX-Q5Wd5WWKSHVDl6n3gJdFo_gvfgjTuy7-hg',
                sheet_name='Sheet1',
                credentials=credentials  # Pass the dictionary here
            )
            db_user = os.getenv("DB_USER")
            db_password = os.getenv("DB_PASSWORD")
            db_host = os.getenv("DB_HOST")
            db_port = os.getenv("DB_PORT")
            db_name = os.getenv("DB_NAME")
            # Store in PostgreSQL
            db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
            store_to_postgresql(df, db_url, 'fashion_data')

        except Exception as e:
            print(f"Terjadi kesalahan dalam proses: {e}")
    else:
        print("Tidak ada data yang ditemukan.")

if __name__ == "__main__":
    main()