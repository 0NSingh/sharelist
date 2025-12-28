import os

postgres_user=os.getenv("POSTGRES_USER")
postgres_dbname=os.getenv("POSTGRES_DBNAME")
postgres_pasword=os.getenv("POSTGRES_PASSWORD")
postgres_host=os.getenv("POSTGRES_HOST")
postgres_url=os.getenv("POSTGRES_URL") if os.getenv("POSTGRES_URL") else URL.create(
    "postgresql+psycopg2",
    username=postgres_user,
    password=postgres_pasword,
    host=postgres_host,
    database=postgres_dbname,
)
