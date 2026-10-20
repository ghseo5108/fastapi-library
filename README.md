
# Library Management API

A simple library management system built with Python and FastAPI.

This project was created as a learning assignment. It stores book data in memory and does not use a database.

## Features

- Get all books
- Add a new book
- Get a book by ID
- Delete a book by ID
- Automatic input validation
- HTTP 404 response when a book is not found

## Requirements

- Python 3.10 or newer
- pip

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd fastapi-library
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the application

```bash
uvicorn main:app --reload
```

The API will be available at:

http://127.0.0.1:8000

## Interactive API Documentation

Open the following URL in your browser:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /books | Get all books |
| POST | /books | Add a new book |
| GET | /books/{id} | Get a book by ID |
| DELETE | /books/{id} | Delete a book by ID |

## Example: Add a Book

Send a POST request to `/books` with this JSON body:

```json
{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "year": 2008
}
```

## Important Note

Book data is stored in memory. Changes made while the application is running are lost when the application restarts.

## Technologies

- Python
- FastAPI
- Pydantic
- Uvicorn
