from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# for sqlite3
# SQLALCHEMY_DATABASE_URL = "sqlite:///./expensetracker.db"

# for postgressql local
# SQLALCHEMY_DATABASE_URL = (
#     "postgresql://postgres:password@localhost/ExpenseTrackerDatabase"
# )

# for supabase
SQLALCHEMY_DATABASE_URL = "postgresql://postgres.girhvaihwupzluuqrmbo:abrarmayaz758@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres"


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()
