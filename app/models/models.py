from sqlalchemy import Integer, String, Column, DECIMAL, CheckConstraint

from app.database import Base


class Book(Base):
    __tablename__ = 'Books'

    id = Column(Integer, primary_key = True, index=True)
    title = Column(String, nullable=True, )
    author = Column(String, nullable=True)
    genre = Column(String,nullable=False)
    year = Column(Integer,nullable=False)
    rating = Column(DECIMAL(2,1),nullable=False)

    __table_args__ = (
        CheckConstraint('year > 0' , name = 'chech_year_positive'),
        CheckConstraint('rating >= 0 and rating <= 10', name = 'check_rating_range')
        
    )