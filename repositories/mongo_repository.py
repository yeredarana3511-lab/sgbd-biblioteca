"""Repositorio MongoDB para bitácora de eventos del sistema."""

from datetime import datetime
from typing import Any

from config.settings import MONGO_COLLECTION_NAME, MONGO_DB_NAME, MONGO_URI

try:
    from pymongo import MongoClient
    from pymongo.errors import PyMongoError, ServerSelectionTimeoutError

    MONGO_AVAILABLE = True
except ImportError:
    MongoClient = None
    PyMongoError = Exception
    ServerSelectionTimeoutError = Exception
    MONGO_AVAILABLE = False


def registrar_evento(
    tipo: str,
    descripcion: str,
    datos: dict[str, Any] | None = None
) -> bool:
    """
    Registra un evento en MongoDB.

    Si MongoDB no está disponible, no rompe el sistema.
    Retorna True si guardó el evento y False si no pudo.
    """
    if not MONGO_AVAILABLE:
        print("[MONGO] pymongo no está instalado. Evento ignorado.")
        return False

    try:
        cliente = MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)
        db = cliente[MONGO_DB_NAME]
        coleccion = db[MONGO_COLLECTION_NAME]

        documento = {
            "tipo": tipo,
            "descripcion": descripcion,
            "datos": datos or {},
            "fecha": datetime.now(),
        }

        coleccion.insert_one(documento)
        cliente.close()
        return True

    except (ServerSelectionTimeoutError, PyMongoError) as error:
        print(f"[MONGO] No se pudo registrar el evento: {error}")
        return False
