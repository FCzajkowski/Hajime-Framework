# ![Hajime 🚀](HAJIME/header.png)
```python
pip install Hajime
```

## 🚀 Aperçu
Hajime est un framework web léger basé sur Python qui fournit un support intégré pour le routage, les middlewares, la gestion des WebSockets, le templating, l'intégration de bases de données et la diffusion de fichiers statiques. Il est conçu pour être simple, flexible et facile à utiliser pour la création d'applications web et d'API.

## 📌 Fonctionnalités
- **Routage** : Prend en charge le traitement des requêtes HTTP avec différentes méthodes
- **Middleware** : Fonctions middleware personnalisées pour le filtrage des requêtes
- **WebSockets** : Support intégré des WebSockets pour les applications en temps réel
- **Templating** : Rendu de templates simple avec remplacement de variables et boucles for
- **Intégration de base de données** : Fonctionne avec les bases de données SQLite et PostgreSQL en utilisant SQLAlchemy
- **Diffusion de fichiers statiques** : Sert efficacement les fichiers depuis un répertoire statique avec mise en cache
- **Gestion des sessions** : Gestion basique des sessions avec cookies
- **Optimisations de performance** : Préchargement des templates et des fichiers statiques

## 📄 Contribuer

Les contributions sont toujours les bienvenues !

Consultez ```contributing.md``` pour savoir comment commencer.

Veuillez respecter le code de conduite de ce projet.

## ✔️ Démarrage rapide
Créez un serveur web simple avec Hajime :

```python
from Hajime import *

app = Hajime()

@app.route("/", methods=["GET"])
def home(environ):
    return "Hello, World!"

if __name__ == "__main__":
    app.launch()
```

Exécutez le script, et le serveur démarrera sur un port disponible. (Par défaut pour Hajime, c'est le port 8000)

## 🛣️ Routage
Hajime fournit un moyen simple de définir des routes avec le décorateur `@app.route`.

```python
@app.route("/hello", methods=["GET"])
def hello(environ):
    return "Hello from Hajime!"
```

Les routes peuvent gérer différentes méthodes HTTP :

```python
@app.route("/submit", methods=["POST"])
def submit(environ):
    data = get_json(environ)
    return json_response({"message": "Data received", "data": data})
```

### Redirection
```python
@app.route("/")
def home(environ):
    return '<h1>hello</h1>'

@app.route("/go-home")
def redirect_home(environ):
    return app.redirect('/')
```

## 🪛 Middleware
Les fonctions middleware peuvent être enregistrées en utilisant `app.use()` pour traiter les requêtes avant de passer le contrôle au gestionnaire de route.

```python
def auth_middleware(environ, params):
    session = environ.get("SESSION", {})
    if not session.get("user"):
        return "Unauthorized access"
    return None

app.use(auth_middleware)
```

## 🛜 WebSockets
Définissez une route WebSocket en utilisant `@app.websocket` :

```python
@app.websocket("/ws")
async def websocket_handler(websocket):
    await websocket.send("Welcome to the WebSocket server!")
    while True:
        message = await websocket.receive()
        await websocket.send(f"You said: {message}")
```

### 📄 Client WebSocket JavaScript
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

## 🌄 Rendu de templates
Hajime prend en charge les templates HTML avec remplacement de variables et boucles for. Les templates sont automatiquement préchargés pour de meilleures performances.

```python
@app.route("/greet")
def greet(environ):
    return app.template("greet.html", name="Alice")
```

### greet.html
```html
<h1>Hello, {{name}}!</h1>
<!-- Exemple de boucle for -->
{% for key, value in items.items() %}
    <p>{{key}}: {{value}}</p>
{% endfor %}
```

## 📅 Support de base de données
Hajime inclut une classe Database qui utilise SQLAlchemy pour interagir avec PostgreSQL et SQLite.

```python
from Hajime import Database

# Connexion à une base de données SQLite
db = Database("sqlite", host="", user="", password="", database="data.db")

# Ou connexion à PostgreSQL
# db = Database("postgresql", host="localhost", user="user", password="pass", database="mydb", port=5432)

# Exécuter des requêtes
db.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
```

Récupération de données :
```python
users = db.fetch_all("SELECT * FROM users")
print(users)

user = db.fetch_one("SELECT * FROM users WHERE id = 1")
print(user)
```

Utilitaires de base de données :
```python
# Obtenir la liste des tables
tables = db.get_tables()

# Obtenir les données d'une table spécifique
users_data = db.get_table_data("users")
```

## 📁 Fichiers statiques
Hajime sert les fichiers statiques depuis le répertoire `static/` et les précharge pour de meilleures performances.

Accédez aux fichiers avec :
```
http://localhost:8000/static/style.css
```

## 💻 Gestion des sessions
Hajime prend en charge la gestion des sessions avec des cookies.

```python
@app.route("/login", methods=["POST"])
def login(environ):
    session_id, session = app.get_session(environ)
    session["user"] = "admin"
    app.set_session(session_id, session)
    return "Logged in!"
```

## 🏃‍♂️ Lancement du serveur
Lancez les serveurs HTTP et WebSocket :
```python
app.launch(port=8000, ws_port=8765)
```

Le framework trouve automatiquement des ports disponibles si ceux spécifiés sont déjà utilisés.

## 🚫 Gestion des erreurs
Des gestionnaires d'erreurs personnalisés peuvent être définis en utilisant :
```python
@app.error_handler(404)
def not_found():
    return "Custom 404 Page Not Found"
```

## 📝 Traitement des données de formulaire
Hajime fournit des utilitaires pour gérer les données de formulaire dans les requêtes POST :

```python
@app.route('/submit-form', methods=["POST"])
def submit_form(environ):
    form_data = environ["form"]
    
    # Vous pouvez maintenant accéder aux champs du formulaire
    name = form_data.get('name', '')
    email = form_data.get('email', '')
    
    # Traiter les données du formulaire
    return f"Form submitted successfully! Name: {name}, Email: {email}"
```

## ➕ Support

Pour obtenir de l'aide, envoyez un email à FCzajkowski@proton.me, ou contactez via X.com : FCzajkowski

---

![Hajime 🚀](HAJIME/footer.png)
