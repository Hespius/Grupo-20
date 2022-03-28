import databases
import sqlalchemy

DATABASE_URL = 'sqlite://>/data.db'

database = databases.Database(DATABASE_URL, force_rollback=False)
metadata = sqlalchemy.MetaData()
