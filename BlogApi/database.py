from sqlalchemy import create_engine
from sqlalchemy .ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



SQlALCHEMY_DATABASE_URL = 'postgresql//postgres:####@localhost/proj-name'
engine = create_engine(SQlALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocomiit=False, autoflush=False, bind=engine)
Base = declarative_base()