from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser
import pathlib
# from pkg_resources import resource_filename

path = pathlib.Path(__file__).parent.joinpath("config.ini")
# path = resource_filename("hogwarts", "config.ini")
file_config = pathlib.Path(path)
config = configparser.ConfigParser()
config.read(file_config)

user = config.get("DB", "user")
password = config.get("DB", "password")
db_name = config.get("DB", "db_name")
domain = config.get("DB", "domain")
port = config.get("DB", "port")

url = f"postgresql://{user}:{password}@{domain}:{port}/{db_name}"

engine = create_engine(url, echo=False)
DBsession = sessionmaker(bind=engine)
session = DBsession()