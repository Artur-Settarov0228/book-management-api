from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session




from app.database.database import get_db
from app.models import Book
from app.schemas.schemas import BookOut,BookCreate, BookUpdate, BookResponse 

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)
@router.get("", response_model = list[BookOut])
async def get_books(
    db:Session= Depends(get_db)):
    Books = db.query(Book).all()

    if not Books:
        raise HTTPException(status_code=404, 
        detail="No books found")
    return Books


@router.get("/{b}")





