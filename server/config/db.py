from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
# import pymysql

database_url = 'mysql://root:@localhost:3306/bid'

engine = create_engine(
    database_url,
)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

# meta = MetaData

Base = declarative_base()



