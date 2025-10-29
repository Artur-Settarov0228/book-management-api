# book-management-api

# 📘 FastAPI Final Exam – Book Management API

## 🎯 Project Overview

Bu final project sizning **FastAPI**, **SQLAlchemy**, va **PostgreSQL** bo‘yicha asosiy bilimlaringizni tekshiradi.
Siz **kitoblarni boshqarish uchun oddiy REST API** yaratishingiz kerak bo‘ladi (CRUD, search, filter).

---

## 🧠 Project Task

Siz **Book Management API** yaratishingiz kerak.
API quyidagi funksiyalarni bajaradi 👇

| Function      | Method | Endpoint                          | Description                                                       |
| ------------- | ------ | --------------------------------- | ----------------------------------------------------------------- |
| Get all books | GET    | `/books`                          | Barcha kitoblarni ko‘rish                                         |
| Get one book  | GET    | `/books/{book_id}`                | ID orqali bitta kitobni olish                                     |
| Create a book | POST   | `/books`                          | Yangi kitob qo‘shish                                              |
| Update a book | PUT    | `/books/{book_id}`                | Kitobni yangilash                                                 |
| Delete a book | DELETE | `/books/{book_id}`                | Kitobni o‘chirish                                                 |
| Search books  | GET    | `/books/search?search=python`     | Title yoki author bo‘yicha qidirish (`search` query param orqali) |
| Filter books  | GET    | `/books/filter?min=2010&max=2020` | Year bo‘yicha filterlash (`min` va `max` query param orqali)      |

---

## 📚 Book Model Fields

Har bir kitob quyidagi maydonlarga ega bo‘lishi kerak:

| Field    | Type    | Description                              |
| -------- | ------- | ---------------------------------------- |
| `id`     | Integer | Unique ID (primary key)                  |
| `title`  | String  | Kitob nomi                               |
| `author` | String  | Muallif                                  |
| `genre`  | String  | Janr (masalan: “Fiction”, “Programming”) |
| `year`   | Integer | Nashr yili                               |
| `rating` | Float   | Reyting (0.0 – 5.0 orasida)              |

**Example JSON:**

```json
{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "genre": "Programming",
  "year": 2008,
  "rating": 4.8
}
```

---

## 🔍 Search va Filter haqida

### 🔎 Search

**Endpoint:**

```
GET /books/search?search=python
```

**Tavsif:**
Title yoki author ichida berilgan so‘z bo‘yicha qidiradi.
Masalan:

```
GET /books/search?search=code
```

→ “code” so‘zi bor kitoblarni qaytaradi.

---

### 🧮 Filter

**Endpoint:**

```
GET /books/filter?min=2010&max=2020
```

**Tavsif:**
`min` va `max` yillar orasidagi kitoblarni chiqaradi.
Masalan:

```
GET /books/filter?min=2000&max=2010
```

→ 2000–2010 oralig‘idagi kitoblar chiqadi.

---

## ⚙️ Technologies Required

### 🔧 Server

* **FastAPI** – asosiy backend framework
* **Uvicorn** – serverni ishga tushirish uchun

### 🗃️ Database & ORM

* **PostgreSQL** – ma’lumotlar bazasi
* **SQLAlchemy** – ORM (ma’lumotlar bilan ishlash)
* **Pydantic** – validation uchun
* **python-dotenv** – environment variables uchun

Jadval yaratish uchun `Base.metadata.create_all()` ishlating.

---

## 📁 Tavsiya etilgan tuzilma

```
book-management-api/
 ┣ app/
 ┃ ┣ main.py
 ┃ ┣ models.py
 ┃ ┣ schemas.py
 ┃ ┣ database.py
 ┃ ┣ routers/
 ┃ ┃ ┣ books.py
 ┃ ┣ __init__.py
 ┣ .env
 ┣ .gitignore
 ┣ requirements.txt
 ┗ README.md
```

---

## ⚙️ Environment Setup

### 1. `.env` fayl

```bash
DB_HOST=
DB_PORT=
DB_USER=
DB_PASS=
DB_NAME=
```

### 2. Kutubxonalarni o‘rnatish

```bash
pip install -r requirements.txt
```

### 3. Loyihani ishga tushirish

```bash
uvicorn app.main:app --reload
```

### 4. Test qilish

Browserda oching:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📦 requirements.txt (example)

```
fastapi
uvicorn
sqlalchemy
psycopg2-binary
pydantic
python-dotenv
```

---

## 🧮 Baholash mezonlari

| Bo‘lim                     | Ball | Tavsif                                |
| -------------------------- | ---- | ------------------------------------- |
| CRUD endpoints             | 40   | Create, Read, Update, Delete ishlaydi |
| SQLAlchemy ORM             | 20   | Model va DB session to‘g‘ri ishlaydi  |
| Search va filter endpoints | 15   | Qidirish va filter ishlaydi           |
| Pydantic validation        | 10   | Schema ishlatilgan                    |
| Error handling             | 10   | HTTPException bilan ishlash           |
| Kod strukturasi            | 5    | Fayllar toza ajratilgan               |

---

## 🚀 Ishni topshirish

* Kodni **GitHub repository** sifatida topshiring.
* Repository nomi: `book-management-api`
* Loyihada quyidagilar bo‘lishi shart:

  * `README.md`
  * `requirements.txt`
  * `.env` fayl namunasi
  * `main.py` orqali ishga tushishi mumkin bo‘lishi kerak:

    ```bash
    uvicorn app.main:app --reload
    ```

---

## 💡 Eslatma

* `.env` faylni to‘g‘ri sozlashni unutmang.
* Barcha endpoints `/docs` sahifasida test qilinadi.
* Kod toza va izchil yozilishi kerak (PEP8 qoidalariga amal qiling).