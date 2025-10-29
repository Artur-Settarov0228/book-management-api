
from app.database.database import Base, engine

Base.metadata.create_all(bind=engine)
