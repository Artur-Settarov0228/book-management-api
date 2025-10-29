from fastapi import APIRouter,Depends,HTTPException,status,Path
from sqlalchemy.orm import Session
from typing import List
import psycopg2

from app.models import Book
from app.database import get_db
from app.schemas import BookOut,BookCreate,BookUpdate
from app.core import config

router = APIRouter(
    prefix='/books',
    tags=['Books']
)

@router.get('',response_model=List[BookOut])
async def get_books(
    db:Session = Depends(get_db)
    ):
    book = db.query(Book).all()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book not found")
    
    return book

@router.get('/filter')
async def search_book_year(
    min:int,
    max:int,
    db:Session = Depends(get_db)
    ):
    
    result = db.query(Book).filter(Book.year.between(min,max)).all()
    return result

@router.get('/{book_id}',response_model=BookOut)
async def get_one_book(
        book_id:int = Path(ge = 1),
        db:Session = Depends(get_db)
    ):
    book = db.query(Book).filter_by(id = book_id).first()

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book not found")
    
    return book

@router.post('',response_model=BookOut)
async def create_book(
    book_data:BookCreate,
    db:Session = Depends(get_db),
    ):
    book = db.query(Book).filter(
        Book.title == book_data.title,
        Book.author == book_data.author,
        Book.genre == book_data.genre,
        Book.year == book_data.year,
        Book.rating == book_data.rating
    ).first()

    if book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book alredy exsits")
    
    new_book = Book(
        title = book_data.title,
        author = book_data.author,
        genre = book_data.genre.value,
        year = book_data.year,
        rating = book_data.rating
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    
    return new_book

@router.delete('/{book_id}')
async def delete_book(
    book_id:int = Path(ge = 1),
    db:Session = Depends(get_db)
    ):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='book not found')
    
    db.delete(book)
    db.commit()
    return {
        'status':'succes'
    }

@router.put('/{book_id}',response_model=BookOut)
async def update_book(
    book_data:BookUpdate,
    book_id:int = Path(ge = 1),
    db:Session = Depends(get_db)
    ):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='book not found')
   
    if book_data.title:
        book.title = book_data.title
    if book_data.author:
        book.author = book_data.author
    if book_data.genre:
        book.genre = book_data.genre
    if book_data.year:
        book.year = book_data.year
    if book_data.rating:
        book.rating = book_data.rating

    db.commit()
    db.refresh(book)
    return book


@router.get('/search')
async def search_book(
    text:str,
    ):
    conn = psycopg2.connect(
        dbname=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASS,
        host=config.DB_HOST, 
        port=config.DB_PORT 
    )
    cur = conn.cursor()

    search_pattern = f'%{text}%' 

    query = "SELECT * FROM books WHERE title ILIKE %s or author ilike %s"
    cur.execute(query, (search_pattern,search_pattern))
    results = cur.fetchone()
    cur.close()
    conn.close()

    return results
