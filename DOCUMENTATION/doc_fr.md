Voici la traduction du markdown en français :


python
Kopiuj
pip install Hajime
🚀 Aperçu
Hajime est un framework web léger basé sur Python qui offre un support intégré pour le routage, le middleware, la gestion des WebSockets, le rendu de templates, l'intégration de bases de données et la gestion des fichiers statiques. Il est conçu pour être simple, flexible et facile à utiliser pour la création d'applications web et d'APIs.

📌 Fonctionnalités
Routage : Gère les requêtes HTTP avec différents types de méthodes
Middleware : Fonctions middleware personnalisées pour le filtrage des requêtes
WebSockets : Prise en charge intégrée des WebSockets pour les applications en temps réel
Rendu de Templates : Rendu simple des templates avec remplacement de variables et boucles for
Intégration de Base de Données : Fonctionne avec les bases de données SQLite et PostgreSQL via SQLAlchemy
Gestion des Fichiers Statiques : Sert efficacement les fichiers à partir d'un répertoire statique avec mise en cache
Gestion des Sessions : Gestion basique des sessions via cookies
Optimisations de Performances : Préchargement des templates et des fichiers statiques
📄 Contribuer
Les contributions sont toujours les bienvenues !

Voir contributing.md pour savoir comment commencer.

Veuillez respecter le code de conduite de ce projet.

✔️ Démarrage Rapide
Créez un serveur web simple avec Hajime :

python
Kopiuj
from Hajime import *

app = Hajime()

@app.route("/", methods=["GET"])
def home(environ):
    return "Bonjour, le monde !"

if __name__ == "__main__":
    app.launch()
Exécutez le script et le serveur démarrera sur un port disponible. (Le port par défaut pour Hajime est le 8000)

🛣️ Routage
Hajime fournit un moyen facile de définir des routes avec le décorateur @app.route.

python
Kopiuj
@app.route("/hello", methods=["GET"])
def hello(environ):
    return "Bonjour depuis Hajime !"
Les routes peuvent gérer différentes méthodes HTTP :

python
Kopiuj
@app.route("/submit", methods=["POST"])
def submit(environ):
    data = get_json(environ)
    return json_response({"message": "Données reçues", "data": data})
Redirection
python
Kopiuj
@app.route("/")
def home(environ):
    return '<h1>Bonjour</h1>'

@app.route("/go-home")
def redirect_home(environ):
    return app.redirect('/')
🪛 Middleware
Les fonctions middleware peuvent être enregistrées avec app.use() pour gérer le traitement des requêtes avant de passer le contrôle au gestionnaire de route.

python
Kopiuj
def auth_middleware(environ, params):
    session = environ.get("SESSION", {})
    if not session.get("user"):
        return "Accès non autorisé"
    return None

app.use(auth_middleware)
🛜 WebSockets
Définir une route WebSocket avec @app.websocket :

python
Kopiuj
@app.websocket("/ws")
async def websocket_handler(websocket):
    await websocket.send("Bienvenue sur le serveur WebSocket !")
    while True:
        message = await websocket.receive()
        await websocket.send(f"Vous avez dit : {message}")
📄 Client WebSocket en JavaScript
html
Kopiuj
<script>
const socket = new WebSocket("ws://localhost:8765/ws");

socket.onopen = () => {
    console.log("Connecté au serveur WebSocket");
    socket.send("Bonjour, Serveur !");
};

socket.onmessage = (event) => {
    console.log("Message du serveur :", event.data);
};

socket.onerror = (error) => {
    console.error("Erreur WebSocket :", error);
};
</script>
🌄 Rendu de Templates
Hajime prend en charge les templates HTML avec remplacement de variables et boucles for. Les templates sont préchargés automatiquement pour de meilleures performances.

python
Kopiuj
@app.route("/greet")
def greet(environ):
    return app.template("greet.html", name="Alice")
greet.html
html
Kopiuj
<h1>Bonjour, {{name}} !</h1>
<!-- Exemple de boucle for -->
{% for key, value in items.items() %}
    <p>{{key}}: {{value}}</p>
{% endfor %}
📅 Prise en Charge des Bases de Données
Hajime inclut une classe Database qui utilise SQLAlchemy pour interagir avec PostgreSQL et SQLite.

python
Kopiuj
from Hajime import Database

# Connexion à la base de données SQLite
db = Database("sqlite", host="", user="", password="", database="data.db")

# Ou connexion à PostgreSQL
# db = Database("postgresql", host="localhost", user="user", password="pass", database="mydb", port=5432)

# Exécution des requêtes
db.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
Récupérer des données :

python
Kopiuj
users = db.fetch_all("SELECT * FROM users")
print(users)

user = db.fetch_one("SELECT * FROM users WHERE id = 1")
print(user)
Utilitaires de base de données :

python
Kopiuj
# Obtenir la liste des tables
tables = db.get_tables()

# Obtenir les données d'une table spécifique
users_data = db.get_table_data("users")
📁 Fichiers Statiques
Hajime sert des fichiers statiques depuis le répertoire static/ et les précharge pour de meilleures performances.

Accédez aux fichiers avec :

bash
Kopiuj
http://localhost:8000/static/style.css
💻 Gestion des Sessions
Hajime prend en charge la gestion des sessions avec des cookies.

python
Kopiuj
@app.route("/login", methods=["POST"])
def login(environ):
    session_id, session = app.get_session(environ)
    session["user"] = "admin"
    app.set_session(session_id, session)
    return "Connecté !"
🏃‍♂️ Lancer le Serveur
Lancez les serveurs HTTP et WebSocket :

python
Kopiuj
app.launch(port=8000, ws_port=8765)
Le framework trouve automatiquement des ports disponibles si ceux spécifiés sont déjà utilisés.

🚫 Gestion des Erreurs
Des gestionnaires d'erreurs personnalisés peuvent être définis avec :

python
Kopiuj
@app.error_handler(404)
def not_found():
    return "Page 404 personnalisée introuvable"
📝 Gestion des Données de Formulaire
Hajime fournit des utilitaires pour gérer les données de formulaire dans les requêtes POST :

python
Kopiuj
@app.route('/submit-form', methods=["POST"])
def submit_form(environ):
    form_data = environ["form"]
    
    # Vous pouvez maintenant accéder aux champs du formulaire
    name = form_data.get('name', '')
    email = form_data.get('email', '')
    
    # Traiter les données du formulaire
    return f"Formulaire soumis avec succès ! Nom : {name}, Email : {email}"
➕ Support
Pour le support, envoyez un email à FCzajkowski@proton.me, ou contactez via X.com : FCzajkowski****
