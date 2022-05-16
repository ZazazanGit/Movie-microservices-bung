#his file contains the actual database model for the REST API

from sqlalchemy import (Column, Integer, MetaData, String, Table, create_engine, ARRAY)        #durch pip install 'databases[postgresql]'
import os                 

from databases import Database

DATABASE_URL = os.getenv('DATABASE_URL')   #URL used to connect to the PostgreSQL database
                                                                                 #movie_user is the name of the database user, 
                                                                                 #movie_password is the password of the database user 
                                                                                 #movie_db is the name of the database           

engine = create_engine(DATABASE_URL)
metadata = MetaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column('casts_id', ARRAY(Integer))
)

database = Database(DATABASE_URL)
