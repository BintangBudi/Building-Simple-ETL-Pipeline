# 🛍️ Fashion Studio Web Scraper & Data Pipeline

This project implements an automated **ETL pipeline** that scrapes product data from the [Fashion Studio](https://fashion-studio.dicoding.dev/) website, processes it, and loads it into:

- 📄 Local CSV file  
- 📊 Google Sheet  
- 🛢️ PostgreSQL database  

---

## 📌 Project Overview

**ETL Workflow:**

- **Extract**: Scrapes book & fashion product data (name, price, rating) using `requests` and `BeautifulSoup`.
- **Transform**: Cleans and structures the data into a `pandas` DataFrame.
- **Load**: Saves data to:
  - CSV (for local access)
  - Google Sheets (for collaboration)
  - PostgreSQL (for scalable storage)

> 🔐 Credentials are managed securely using environment variables via `.env`.

---

## ⚙️ Tech Stack

- **Language**: Python 3  
- **Libraries**:
  - Web Scraping: `requests`, `beautifulsoup4`
  - Data Processing: `pandas`
  - Database: `SQLAlchemy`, `psycopg2-binary`
  - Google Sheets API: `google-api-python-client`, `google-auth-httplib2`, `google-auth-oauthlib`
  - Env Management: `python-dotenv`

---

## 🚀 Setup & Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2. Create Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
## Create a requirements.txt file with the following content:
```bash
requests
beautifulsoup4
pandas
sqlalchemy
psycopg2-binary
google-api-python-client
google-auth-httplib2
google-auth-oauthlib
python-dotenv
```
## Then run:
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
## Copy the template file and fill in your credentials:
```bash
cp .env.example .env
```

