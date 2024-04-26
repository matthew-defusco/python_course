from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Float, Integer

# Initialize the db
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

##### MODELS #####
class Book(db.Model):
  id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
  title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
  author: Mapped[str] = mapped_column(String(250), nullable=False)
  rating: Mapped[float] = mapped_column(Float, nullable=False)
