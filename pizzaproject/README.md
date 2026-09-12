# Pizza API

A Django REST Framework API for browsing pizzas and their ingredients.

## Requirements

- Python 3.13 or later
- SQLite (included with Python)

## Setup

From the directory containing `manage.py`:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows Command Prompt
.venv\Scripts\activate.bat

# macOS/Linux
source .venv/bin/activate
```

Install dependencies and prepare the database:

```bash
pip install -r requirements.txt
python manage.py migrate
```

## Run the API

```bash
python manage.py runserver
```

The development server runs at `http://127.0.0.1:8000/`.

## Endpoints

All API endpoints are prefixed with `/api/`.

| Method | Endpoint                                  | Description                                              |
| ------ | ----------------------------------------- | -------------------------------------------------------- |
| `GET`  | `/api/pizzas/`                            | Return all pizzas with their ingredients                 |
| `GET`  | `/api/pizzas/<name>/`                     | Return one pizza by its exact name                       |
| `GET`  | `/api/pizzas/ingredient/<ingredient>/`    | Return pizzas containing an ingredient, case-insensitive |
| `GET`  | `/api/pizzas/filter/?ingredients=<a>,<b>` | Return pizzas containing any listed ingredient           |

Examples:

```bash
curl http://127.0.0.1:8000/api/pizzas/
curl http://127.0.0.1:8000/api/pizzas/queen/
curl http://127.0.0.1:8000/api/pizzas/ingredient/tomato/
curl "http://127.0.0.1:8000/api/pizzas/filter/?ingredients=tomato,mozzarella"
```

The ingredient filter requires the `ingredients` query parameter. If it is omitted, the API returns `400` with `{"error":"missing ingredients"}`. An unknown pizza name returns `404` with `{"error":"Pizza not found"}`.

## Response shape

A pizza includes its `id`, `name`, and nested ingredients. Each ingredient includes `id`, `name`, `price`, and `calories`.

```json
{
  "id": 1,
  "name": "queen",
  "ingredients": [
    {
      "id": 1,
      "name": "tomato",
      "price": "1.50",
      "calories": 20
    }
  ]
}
```

## Project layout

- `pizzaproject/`: Django project configuration and URL routing
- `pizzas/`: models, serializers, API views, migrations, and tests
- `db.sqlite3`: local development database
- `manage.py`: Django command-line entry point

## Development checks

Run Django's system checks and tests with:

```bash
python manage.py check
python manage.py test
```
