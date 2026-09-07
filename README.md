# Book Store App

A Flask book store application with user accounts, a book catalog, shopping cart, coupons, checkout, orders, and admin pages.

## Project Structure

- `App.py` - Flask application and routes
- `templates/` - HTML pages and JSON data files used by the app
- `models/` - Python domain models
- `db setup/` - database models and database helpers
- `json/` - JSON data helpers

## Start the App Locally

### Prerequisites

- Python 3.10 or newer

### Windows

Open PowerShell and move to the project folder:

```powershell
cd "C:\path\to\Book Store App"
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install the dependencies and start the app:

```powershell
python -m pip install Flask SQLAlchemy
python App.py
```

### macOS

Open Terminal and move to the project folder:

```bash
cd "/Users/macbook/Downloads/Book Store App"
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies and start the app:

```bash
python -m pip install Flask SQLAlchemy
python App.py
```

### Open the app

After starting the Flask app on either operating system, open:

```text
http://127.0.0.1:5000
```

You can also use `http://localhost:5000`. Keep the terminal running while using the app. Stop the server with `Ctrl+C`.

## Important: Use the Local Flask Server

Do **not** open any HTML file directly from the folders or by using a `file://` URL. The files in `templates/` are Flask templates and depend on routes, sessions, and backend data.

Always start `App.py` and open the localhost address:

```text
http://127.0.0.1:5000
```

Using the local Flask server allows the app to call the API and backend routes correctly.

## Troubleshooting

### `ModuleNotFoundError: No module named 'flask'`

Activate the virtual environment for your operating system and install the dependencies again:

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install Flask SQLAlchemy
```

macOS:

```bash
source .venv/bin/activate
python -m pip install Flask SQLAlchemy
```

### The browser cannot connect

Confirm that `python App.py` is still running and that you opened `http://127.0.0.1:5000`, not an HTML file directly.

### Database or JSON files are not found

Run `App.py` from the project root, where `App.py` is located. Do not start it from inside `templates/`, `json/`, or another subfolder.

Windows PowerShell:

```powershell
cd "C:\path\to\Book Store App"
python App.py
```

macOS:

```bash
cd "/Users/macbook/Downloads/Book Store App"
python App.py
```
