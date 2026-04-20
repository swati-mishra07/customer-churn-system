import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

# Load env variables
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

# Create connection
engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

# Load CSV
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, 'data', 'churn_results.csv')

df = pd.read_csv(file_path)

# Push to SQL
df.to_sql('churn_predictions', engine, if_exists='replace', index=False)

print("Data uploaded to SQL")