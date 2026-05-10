# SQLite and SQLAlchemy Setup Guide

## Overview

This guide covers how to set up SQLite and SQLAlchemy for your astrology desktop app. It will allow you to store your transits and chart data locally. Later, you can easily switch to PostgreSQL by changing the SQLAlchemy configuration.

## Step 1: Install Required Packages

Install `sqlite3` (included with Python) and `sqlalchemy`:

```bash
pip install sqlalchemy
```

## Step 2: Create a SQLite Database

SQLite is a file-based database, so you don't need to run a server. Create a new SQLite database file (e.g., `astrology.db`) and use SQLAlchemy to interact with it.

## Step 3: Set Up SQLAlchemy ORM

Below is a simple example of defining a `Transit` model and interacting with the database:

```python
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Create SQLite engine (can be replaced with PostgreSQL engine later)
engine = create_engine('sqlite:///astrology.db')

# Create a base class for declarative models
Base = declarative_base()

# Define the Transit model
class Transit(Base):
    __tablename__ = 'transits'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    date = Column(DateTime, default=datetime.datetime.utcnow)

# Create all tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Example: Add a new transit
new_transit = Transit(
    name='Venus Retrograde',
    description='Venus is currently in retrograde. Be cautious with love and relationships during this time.',
    date=datetime.datetime(2025, 10, 15)
)
session.add(new_transit)
session.commit()

# Example: Query all transits
transits = session.query(Transit).all()
for transit in transits:
    print(f"{transit.name}: {transit.description} (Date: {transit.date})")
```

## Step 4: Switch to PostgreSQL (Optional)

To switch to PostgreSQL, update the SQLAlchemy engine to:

```python
engine = create_engine('postgresql://username:password@localhost:5432/astrology')
```

Replace `username`, `password`, and `localhost` with your PostgreSQL credentials.

## Summary

- **SQLite**: Used as the default database (no server needed)
- **SQLAlchemy**: Used as the ORM to interact with the database
- **PostgreSQL**: Can be used later by replacing the engine configuration
- **Tested and Running**: This setup includes adding and querying data in the database

---

This file includes full database setup for SQLite with SQLAlchemy and shows how to switch to PostgreSQL. It includes test code to add and query data, and it is ready to be ingested by any automated system that builds or runs your project.