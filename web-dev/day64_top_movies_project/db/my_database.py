from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy

# CREATE DB
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
