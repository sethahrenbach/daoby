from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.settings import CONFIGS

conf = CONFIGS['database']

engine = create_engine(f'{conf["lang"]}://{conf["user"]}:{conf["pass"]}@{conf["host"]}:{conf["port"]}/{conf["name"]}',
                       echo=conf["enable_logs"])
session = sessionmaker(bind=engine)()

BaseModel = declarative_base()


def setup_database():
    BaseModel.metadata.create_all(engine)
