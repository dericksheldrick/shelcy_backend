# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = 'sqlite:///shelcy.db'

# engine = create_engine(DATABASE_URL, echo=True)
# Session = sessionmaker(bind=engine)
# session = Session() #Starting our db

# Base = declarative_base()

# database.py
# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
DATABASE_URL = 'sqlite:///shelcy.db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

