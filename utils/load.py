import psycopg2
from sqlalchemy import create_engine
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def store_to_csv(df, file_path='output.csv'):
    """Menyimpan DataFrame ke dalam file CSV."""
    try:
        df.to_csv(file_path, index=False)
        print(f"Data berhasil disimpan ke file CSV: {file_path}")
    except Exception as e:
        print(f"Gagal menyimpan data ke file CSV: {e}")

def append_df_to_google_sheets(df, spreadsheet_id, sheet_name, credential_file):
    try:
        # Set up credentials and build service
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        credentials = Credentials.from_service_account_file(credential_file, scopes=scopes)
        service = build('sheets', 'v4', credentials=credentials)
        sheet = service.spreadsheets()

        # Check if the sheet is empty by trying to read cell A1
        result = sheet.values().get(
            spreadsheetId=spreadsheet_id,
            range=f'{sheet_name}!A1'
        ).execute()

        # If 'values' key not in result, it's empty
        if 'values' not in result:
            print("📋 Sheet is empty, adding column headers.")
            values = [df.columns.tolist()] + df.values.tolist()
        else:
            print("📄 Sheet already has data, appending only new rows.")
            values = df.values.tolist()

        # Prepare the request body
        body = {'values': values}

        # Append the data
        sheet.values().append(
            spreadsheetId=spreadsheet_id,
            range=sheet_name,
            valueInputOption='RAW',
            insertDataOption='INSERT_ROWS',
            body=body
        ).execute()

        print("✅ Data successfully written to Google Sheets!")
    except Exception as e:
        print(f"❌ Error occurred: {e}")


def store_to_postgresql(df, db_url, table_name):
    # Create a connection to the PostgreSQL database
    engine = create_engine(db_url)

    # Save the dataframe to PostgreSQL
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"Data saved to PostgreSQL table {table_name}.")
