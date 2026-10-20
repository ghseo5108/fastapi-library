
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Library Management API",
    description="A simple library management system built with FastAPI",
    version="1.0.0"
)

# Data stored in memory (no database)
books = [
    {
        "id": 1,
        "title": "Atomic Habits",
        "author": "James Clear",
        "year": 2018
    },
    {
        "id": 2,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "year": 1988
    }
]


# Structure of a new book
class BookCreate(BaseModel):
    title: str
    author: str
    year: int


# GET /books - Get all books
@app.get("/books")
def get_books():
    return books


# POST /books - Add a new book
@app.post("/books", status_code=201)
def add_book(book: BookCreate):
    new_id = max((item["id"] for item in books), default=0) + 1

    new_book = {
        "id": new_id,
        "title": book.title,
        "author": book.author,
        "year": book.year
    }

    books.append(new_book)
    return new_book


# GET /books/{id} - Get one book
@app.get("/books/{id}")
def get_book(id: int):
    for book in books:
        if book["id"] == id:
            return book

    raise HTTPException(status_code=404, detail="Book not found")


# DELETE /books/{id} - Delete one book
@app.delete("/books/{id}")
def delete_book(id: int):
    for index, book in enumerate(books):
        if book["id"] == id:
            deleted_book = books.pop(index)
            return {
                "message": "Book deleted successfully",
                "book": deleted_book
            }

    raise HTTPException(status_code=404, detail="Book not found")
