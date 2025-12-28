from sqlalchemy import create_engine
from constants import postgres_url

class DBService():
    def __init__(self):
        self.engine=create_engine(postgres_url)
        