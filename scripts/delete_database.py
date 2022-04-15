import sqlalchemy

from api.database import DATABASE_URL, metadata


def config_db(database_url=DATABASE_URL):
    engine = sqlalchemy.create_engine(database_url)
    metadata.drop_all(engine)


if __name__ == '__main__':
    config_db()
