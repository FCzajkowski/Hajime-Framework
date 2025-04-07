![Hajime 🚀](/images/header.png)
```python
pip install Hajime
```
### https://pypi.org/project/Hajime/


## 🚀 Overview
Hajime is a lightweight Python-based web framework that provides built-in support for routing, middleware, WebSocket handling, templating, database integration, and static file serving. It is designed to be simple, flexible, and easy to use for building web applications and APIs.

## 📌 Features
- **Routing**: Supports HTTP request handling with different methods
- **Middleware**: Custom middleware functions for request filtering
- **WebSockets**: Built-in WebSocket support for real-time applications
- **Templating**: Simple template rendering with variable replacement and for-loops
- **Database Integration**: Works with SQLite and PostgreSQL databases using SQLAlchemy
- **Static File Serving**: Efficiently serves files from a static directory with caching
- **Session Management**: Basic session handling with cookies
- **Performance Optimizations**: Preloading of templates and static files

## 📄 Contributing

Contributions are always welcome!

See ```contributing.md``` for ways to get started.

Please adhere to this project's code of conduct.

## ✔️ Quick Start
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

Run the script, and the server will start at an available port. (Default for Hajime is 8000)

## 🛣️ Routing
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

### Redirecting
```python
@app.route("/")
def home(environ):
    return '<h1>hello</h1>'

@app.route("/go-home")
def redirect_home(environ):
    return app.redirect('/')
```

## 🪛 Middleware
Middleware functions can be registered using `app.use()` to handle request processing before passing control to the route handler.

```python
def auth_middleware(environ, params):
    session = environ.get("SESSION", {})
    if not session.get("user"):
        return "Unauthorized access"
    return None

app.use(auth_middleware)
```

## 🛜 WebSockets
Define a WebSocket route using `@app.websocket`:

```python
@app.websocket("/ws")
async def websocket_handler(websocket):
    await websocket.send("Welcome to the WebSocket server!")
    while True:
        message = await websocket.receive()
        await websocket.send(f"You said: {message}")
```

### 📄 JavaScript WebSocket Client
```html
<script>
const socket = new WebSocket("ws://localhost:8765/ws");

socket.onopen = () => {
    console.log("Connected to WebSocket server");
    socket.send("Hello, Server!");
};

socket.onmessage = (event) => {
    console.log("Message from server:", event.data);
};

socket.onerror = (error) => {
    console.error("WebSocket error:", error);
};
</script>
```

## 🌄 Template Rendering
Hajime supports HTML templates with variable replacement and for-loops. Templates are automatically preloaded for better performance.

```python
@app.route("/greet")
def greet(environ):
    return app.template("greet.html", name="Alice")
```

### greet.html
```html
<h1>Hello, {{name}}!</h1>
<!-- For-loop example -->
{% for key, value in items.items() %}
    <p>{{key}}: {{value}}</p>
{% endfor %}
```

## 📅 Database Support
Hajime includes a Database class that leverages SQLAlchemy to interact with PostgreSQL and SQLite.

```python
from Hajime import Database

# Connect to SQLite database
db = Database("sqlite", host="", user="", password="", database="data.db")

# Or connect to PostgreSQL
# db = Database("postgresql", host="localhost", user="user", password="pass", database="mydb", port=5432)

# Execute queries
db.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
```

Fetching data:
```python
users = db.fetch_all("SELECT * FROM users")
print(users)

user = db.fetch_one("SELECT * FROM users WHERE id = 1")
print(user)
```

Database utilities:
```python
# Get list of tables
tables = db.get_tables()

# Get data from a specific table
users_data = db.get_table_data("users")
```

## 📁 Static Files
Hajime serves static files from the `static/` directory and preloads them for better performance.

Access files with:
```
http://localhost:8000/static/style.css
```

## 💻 Session Management
Hajime supports session handling with cookies.

```python
@app.route("/login", methods=["POST"])
def login(environ):
    session_id, session = app.get_session(environ)
    session["user"] = "admin"
    app.set_session(session_id, session)
    return "Logged in!"
```

## 🏃‍♂️ Running the Server
Launch the HTTP and WebSocket servers:
```python
app.launch(port=8000, ws_port=8765)
```

The framework automatically finds available ports if the specified ones are in use.

## 🚫 Error Handling
Custom error handlers can be defined using:
```python
@app.error_handler(404)
def not_found():
    return "Custom 404 Page Not Found"
```

## 📝 Form Data Handling
Hajime provides utilities to handle form data in POST requests:

```python
@app.route('/submit-form', methods=["POST"])
def submit_form(environ):
    form_data = environ["form"]
    
    # Now you can access form fields
    name = form_data.get('name', '')
    email = form_data.get('email', '')
    
    # Process the form data
    return f"Form submitted successfully! Name: {name}, Email: {email}"
```

## ➕ Support

For support, 
#### email FCzajkowski@proton.me, or Contact through X.com: 
### @FCzajkowski

---

![Hajime 🚀](/images/footer.png)

