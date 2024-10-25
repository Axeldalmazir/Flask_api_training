# Flask Drink API

This is a simple Flask application that provides an API for managing drinks using SQLite as the database.

## Features

- Add a new drink
- Retrieve a list of all drinks
- Retrieve a specific drink by ID
- Delete a drink by ID

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. **Set up a virtual environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use .venv\Scripts\activate

3. **Install the required packages**:

   ```bash
   pip install Flask Flask-SQLAlchemy

3. **Run the application**:

    ```bash
    python app.py

The API will be available at http://127.0.0.1:5000.

## API Endpoints

- GET /

  Returns a simple greeting message.

- GET /drinks

  Returns a JSON object containing a list of all drinks.

- GET /drinks/<id>

  Retrieves a specific drink by its ID.

- POST /drinks

  Adds a new drink. Requires a JSON body with name and description.

- DELETE /drinks/<id>

  Deletes a drink by its ID.
