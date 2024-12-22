from sqlalchemy import create_engine,URL
from sqlalchemy.orm import declarative_base, sessionmaker
import pymysql
from environs import Env

env = Env()
env.read_env()

pymysql.install_as_MySQLdb()

url = URL.create(
    drivername='mysql+pymysql',
    username=env.str("MYSQL_USER"),
    password=env.str("MYSQL_PASSWORD"),
    host=env.str("MYSQL_HOST"),
    port=3307,
    database=env.str("MYSQL_DATABASE")
).render_as_string(hide_password=False)

engine = create_engine(url)

Base = declarative_base()

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


