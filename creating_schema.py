from sqlalchemy_setup import *
from sqlalchemy import text

ddl_query = """
-- Create schema for isolation
CREATE SCHEMA IF NOT EXISTS bronze;

CREATE TABLE IF NOT EXISTS bronze.raw_flights (
    id SERIAL PRIMARY KEY,
    payload JSONB NOT NULL,            -- The exact raw JSON object for 1 flight
    extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Metadata: when we ingested it
);
"""

with engine.begin() as connection:
    connection.execute(text(ddl_query))