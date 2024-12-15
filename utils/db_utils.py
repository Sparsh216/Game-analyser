'''
DB Utils
'''
from datetime import datetime
from models.dataModel.db_model import Game


def parse_release_date(date_str):
    '''
    Parses dates
    '''
    try:
        # Attempt parsing with known date formats
        return datetime.strptime(date_str.strip(), "%b %Y").date()
    except ValueError:
        try:
            return datetime.strptime(date_str.strip(), "%d %b, %Y").date()
        except ValueError:
            return None

def put_in_postgres(csv_reader, db):
    '''
    Put data in db
    '''
    for row in csv_reader:
        if db.query(Game).filter(Game.AppID == row['AppID']).first():
            continue
        game = Game(
            AppID=int(row['AppID']),
            Name=row['Name'],
            Release_date=row['Release date'],
            Required_age=int(row['Required age']),
            Price=float(row['Price']),
            DLC_count=int(row['DLC count']),
            About_the_game=row['About the game'],
            Supported_languages=str(row['Supported languages']),
            Windows=row['Windows'].lower() == 'true',
            Mac=row['Mac'].lower() == 'true',
            Linux=row['Linux'].lower() == 'true',
            Positive=int(row['Positive']),
            Negative=int(row['Negative']),
            Score_rank=int(row['Score rank']) if row['Score rank'] else None,
            Developers=row['Developers'],
            Publishers=row['Publishers'],
            Categories=row['Categories'],
            Genres=row['Genres'],
            Tags=row['Tags']
        )
        db.add(game)
