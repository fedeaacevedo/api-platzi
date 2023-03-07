from config.database import Base
from sqlalchemy import Column, Float, Integer, String

#creamos la base de datos con sus tablas
class Movie(Base):
    __tablename__= "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)