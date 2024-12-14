from sqlalchemy import Column, Integer, BigInteger, String, Float, Date, Boolean, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker 

# Base class setup
Base = declarative_base()

# Game model definition
class Game(Base):
    '''
    game model
    '''
    __tablename__ = "games"

    AppID = Column(BigInteger, unique=True, nullable=False,primary_key=True,)  # app_id
    Name = Column(String, nullable=True)  # name
    Release_date = Column("Release Date",String, nullable=True)  # release_date
    Required_age = Column(Integer, nullable=True)  # required_age
    Price = Column(Float, nullable=True)  # price
    DLC_count = Column(Integer, nullable=True)  # dlc_count
    About_the_game = Column(String, nullable=True)  # about
    Supported_languages = Column(String, nullable=True)  # languages
    Windows = Column(Boolean, default=False)  # windows
    Mac = Column(Boolean, default=False)  # mac
    Linux = Column(Boolean, default=False)  # linux
    Positive = Column(Integer, nullable=True)  # positive
    Negative = Column(Integer, nullable=True)  # negative
    Score_rank = Column(Integer, nullable=True)  # score_rank
    Developers = Column(String, nullable=True)  # developers
    Publishers = Column(String, nullable=True)  # publishers
    Categories = Column(String, nullable=True)  # categories
    Genres = Column(String, nullable=True)  # genres
    Tags = Column(String, nullable=True)

# Database configuration
DB_USERNAME = "game_db_7we4_user"
DB_PASSWORD = "kUtlLpadvJFSi6LpvIQa3ZNy8clECWdD"
DB_HOST = "dpg-ctere5tds78s73djh81g-a.oregon-postgres.render.com"
DB_PORT = 5432
DATABASE = "game_db_7we4"
db_url = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DATABASE}"

def initialize_database():
    '''
    init database
    '''

    print(f"Connecting to {db_url}...")
    engine = create_engine(db_url)

    try:
        if not database_exists(engine.url):
            create_database(engine.url)
            print(f"Database '{DATABASE}' created.")
        else:
            print(f"Database '{DATABASE}' already exists.")

        Base.metadata.create_all(engine)
        print("Tables created or already exist.")
    except Exception as e:
        print(f"Error during table creation: {e}")

    print("Initialization complete.")


def get_session():
    """Return a new database session."""
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    return Session()
