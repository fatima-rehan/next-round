from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "sqlite:///../data/next_round.db" # tells SQLAlchemy to use SQLite and where to store database

engine = create_engine(DATABASE_URL, connect_args = {"check_same_thread" : False}) # creates connection to database

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine) # creates session factory to talk to database

# creates all tables in database if they don't exist
def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database initialized!")


# gives each request its own database session
def get_db():
    db = SessionLocal()
    try:
        yield db  # stays open during request, closes after
    finally:
        db.close()



