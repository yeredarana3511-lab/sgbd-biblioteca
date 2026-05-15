import os

# Configuración SQLite
# Apunta dinámicamente a la carpeta data/ en la raíz del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
SQLITE_DB_PATH = os.path.join(DATA_DIR, "biblioteca.db")

# Configuración MongoDB
MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB_NAME = "biblioteca_logs"
MONGO_COLLECTION_NAME = "bitacora"

