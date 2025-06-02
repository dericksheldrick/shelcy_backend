# Shelcy Backend

This is the backend setup for Shelcy e-commerce platform. It uses **Python** and **SQLAlchemy** to define models, and a `seed.py` script to populate the database with users and products.



## Features

- user model with avatar support
- product model with multiple images and categories
- seed script to populate users and products
- SQLite is used as the local development database



## Tech stack 

- Python 3
- Sqlite
- SQLAlchemy (ORM)
- dotenv (for environment variables)
- db.json (for generating data)

## Project structure 

```shelcy-backend/
│
├── app.py
├── database.py
├── models.py
├── seed.py # Script to populate the database
├── db.json # Product and user data used in seeding
└── README.md
```

## How to run locally
- Clone the repo, set up a virtual environment, and run `python seed.py`

## Avatar URLS
Avatar images are dynamically generated using Robohash, based on the user's email or username.

## Future Expansion Ideas
- orders, cart items, and Reviews tables(currently empty)
- API server using Flask or FastAPI
- User authentication and role management
- Admin dashboard for managing products

---

Built by `DERICK` - part of my full-stack project 

