# The Blogs

A shared blogging platform built for the Web Engineering course project.

## Overview

The Blogs is a web application where visitors can browse, filter, and search
blog posts. Registered users can log in and publish, edit, or delete their own posts.

## Features

- Browse all posts (paginated, newest first)
- Filter posts by author or date
- Search posts by title keyword
- User registration and login
- Create, edit, and delete own posts

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11+ |
| Web framework | Flask |
| ORM | Flask-SQLAlchemy |
| Auth | Flask-Login + Werkzeug password hashing |
| Database | SQLite (development) |
| Templates | Jinja2 |
| Package manager | uv |
| Linter / Formatter | Ruff |
| Testing | pytest + pytest-cov |

## Project Structure

```
the-blogs/
├── app/
│   ├── __init__.py       # App factory
│   ├── models.py         # User, Post models
│   ├── routes.py         # URL routes and views
│   ├── auth.py           # Registration and login
│   ├── templates/        # Jinja2 HTML templates
│   └── static/           # CSS and JS assets
├── tests/
│   └── test_basic.py     # Placeholder tests
├── pyproject.toml        # Project config, dependencies, tool settings
├── .gitignore
└── README.md
```

## Setup

### Prerequisites

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) if not already available:

```powershell
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Install and run

```powershell
# Clone the repository
git clone https://github.com/<your-username>/the-blogs.git
cd the-blogs

# Create virtual environment and install dependencies
uv sync --extra dev

# Run the development server
uv run flask --app app run --debug
```

Open your browser at `http://127.0.0.1:5000`.

## Development

```powershell
# Run linter
uv run ruff check .

# Auto-fix lint issues
uv run ruff check --fix .

# Run formatter
uv run ruff format .

# Run tests with coverage
uv run pytest --cov=app --cov-report=term-missing
```
