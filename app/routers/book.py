from fastapi import APIRouter, Depends, HTTPException, Path, status
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


@router.get('/filter')
async def filter_books(
    min :int,
    max :int,
    db:Session= Depends(get_db)):

     result = db.query(Book).filter(Book.year.between(min, max)).all()
     return result

@router.get("/{book_id}", response_model=BookOut)
async def get_book_by_id(
    book_id: int = Path(ge = 1),
    db:Session= Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, 
        detail=f"Book with id {book_id} not found")
    return book



@router.post('', response_model=BookOut, status_code=status.HTTP_201_CREATED)
async def create_book(
    book_data: BookCreate,
    db: Session = Depends(get_db),
):
    # Kitob mavjudligini tekshirish
    book = db.query(Book).filter(
        Book.title == book_data.title,
        Book.author == book_data.author,
        Book.year == book_data.year
    ).first()

    if book:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Book already exists"
        )
    
    # Yangi kitob yaratish
    new_book = Book(
        title=book_data.title,
        author=book_data.author,
        genre=book_data.genre.value,  # Agar Enum bo'lsa
        year=book_data.year,
        rating=book_data.rating
    )
    
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    
    return new_book