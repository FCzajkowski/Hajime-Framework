![Hajime 🚀](HAJIME/header.png)

## Overview
Hajime is a lightweight Python-based web framework that provides built-in support for routing, middleware, WebSocket handling, templating, and database interaction. It is designed to be simple, flexible, and easy to use for building web applications and APIs.

## Features
- **Routing**: Supports HTTP request handling with different methods.
- **Middleware**: Custom middleware functions for request filtering.
- **WebSockets**: Built-in WebSocket support for real-time applications.
- **Templating**: Simple template rendering using HTML files.
- **Database Integration**: Works with SQLite and PostgreSQL databases.
- **Static File Serving**: Serves files from a static directory.
- **Session Management**: Basic session handling with cookies.

## Installation
Hajime does not require external dependencies other than SQLAlchemy for database support. Install the necessary dependencies:
```sh
pip install sqlalchemy psycopg2-binary websockets
```

## Quick Start
Create a simple web server with Hajime:

```python
from Hajime import *

app = Hajime()

@app.route("/", methods=["GET"])
def home(environ):
    return "Hello, World!"

if __name__ == "__main__":
    app.launch()
```

Run the script, and the server will start at an available port.

## Routing
Hajime provides an easy way to define routes with the `@app.route` decorator.

```python
@app.route("/hello", methods=["GET"])
def hello(environ):
    return "Hello from Hajime!"
```

Routes can handle different HTTP methods:

```python
@app.route("/submit", methods=["POST"])
def submit(environ):
    data = get_json(environ)
    return json_response({"message": "Data received", "data": data})
```

## Middleware
Middleware functions can be registered using `app.use()` to handle request processing before passing control to the route handler.

```python
def auth_middleware(environ, params):
    session = environ.get("SESSION", {})
    if not session.get("user"):
        return "Unauthorized access"
    return None

app.use(auth_middleware)
```

## WebSockets
Define a WebSocket route using `@app.websocket`:

```python
@app.websocket("/ws")
async def websocket_handler(websocket):
    await websocket.send("Welcome to the WebSocket server!")
```

## Template Rendering
Hajime supports simple HTML templates with variable replacement.

```python
@app.route("/greet")
def greet(environ):
    return app.template("greet.html", name="Alice")
```

### `greet.html`
```html
<h1>Hello, {{name}}!</h1>
```

## Database Support
Hajime includes a `Database` class to interact with PostgreSQL and SQLite.

```python
from Hajime import Database

db = Database("sqlite", database="data.db")

db.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
```

Fetching data:
```python
users = db.fetch_all("SELECT * FROM users")
print(users)
```

## Static Files
Serve static files from the `static/` directory.

Access files with:
```
http://localhost:8000/static/style.css
```

## Session Management
Hajime supports session handling with cookies.

```python
@app.route("/login", methods=["POST"])
def login(environ):
    session_id, session = app.get_session(environ)
    session["user"] = "admin"
    app.set_session(session_id, session)
    return "Logged in!"
```

## Running the Server
Launch the HTTP and WebSocket servers:
```python
app.launch(port=8000, ws_port=8765)
```

## Error Handling
Custom error handlers can be defined using:
```python
@app.error_handler(404)
def not_found():
    return "Custom 404 Page Not Found"
```

![Hajime 🚀](HAJIME/footer.png)
