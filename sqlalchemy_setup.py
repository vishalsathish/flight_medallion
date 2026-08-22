from sqlalchemy import create_engine

# params for creating url in engine
USER = "de_user"
PASSWORD = "de_password"
HOST = "postgres"
PORT = 5432
DB_NAME = "aviation_db"

url = "postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:5432/{DB_NAME}"

# engine new connection
engine = create_engine(url, echo=True)