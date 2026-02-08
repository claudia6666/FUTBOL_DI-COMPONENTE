from PySide6.QtSql import QSqlDatabase, QSqlQuery
import os
import sys
from models.initial_data import insertar_datos_iniciales
def get_db_path():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_path, "models", "torneoFutbol_sqlite.db")
    return db_path
def conectar():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db_path = get_db_path()
    db.setDatabaseName(db_path)
    if not db.open():
        raise Exception("No se pudo abrir la base de datos")
    query = QSqlQuery(db)
    query.exec("PRAGMA foreign_keys = ON;")
    crear_tablas(db)
    insertar_datos_iniciales(db)
    print("Base de datos conectada y tablas creadas correctamente")
    return db
def crear_tablas(db):
    query = QSqlQuery(db)
    query.exec("""
    CREATE TABLE IF NOT EXISTS equipos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL UNIQUE,
        curso TEXT NOT NULL,
        color_camiseta TEXT,
        fecha_creacion TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)
    query.exec("""
    CREATE TABLE IF NOT EXISTS participantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        fecha_nacimiento TEXT,
        curso TEXT,
        tipo_participante TEXT NOT NULL,
        posicion TEXT,
        equipo_id INTEGER,
        tarjetas_amarillas INTEGER DEFAULT 0,
        tarjetas_rojas INTEGER DEFAULT 0,
        goles INTEGER DEFAULT 0,
        fecha_registro TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (equipo_id) REFERENCES equipos(id) ON DELETE SET NULL
    )
    """)
    query.exec("""
    CREATE TABLE IF NOT EXISTS partidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        equipo1_id INTEGER NOT NULL,
        equipo2_id INTEGER NOT NULL,
        arbitro_id INTEGER,
        goles_equipo1 INTEGER DEFAULT 0,
        goles_equipo2 INTEGER DEFAULT 0,
        fecha TEXT NOT NULL,
        hora TEXT,
        ronda TEXT,
        estado TEXT DEFAULT 'Programado',
        fecha_creacion TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (equipo1_id) REFERENCES equipos(id) ON DELETE CASCADE,
        FOREIGN KEY (equipo2_id) REFERENCES equipos(id) ON DELETE CASCADE,
        FOREIGN KEY (arbitro_id) REFERENCES participantes(id) ON DELETE SET NULL
    )
    """)
    query.exec("""
    CREATE TABLE IF NOT EXISTS goles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        participante_id INTEGER NOT NULL,
        partido_id INTEGER NOT NULL,
        minuto INTEGER,
        fecha_registro TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (participante_id) REFERENCES participantes(id) ON DELETE CASCADE,
        FOREIGN KEY (partido_id) REFERENCES partidos(id) ON DELETE CASCADE
    )
    """)
    query.exec("""
    CREATE TABLE IF NOT EXISTS tarjetas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        participante_id INTEGER NOT NULL,
        partido_id INTEGER NOT NULL,
        tipo TEXT NOT NULL,
        minuto INTEGER,
        fecha_registro TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (participante_id) REFERENCES participantes(id) ON DELETE CASCADE,
        FOREIGN KEY (partido_id) REFERENCES partidos(id) ON DELETE CASCADE
    )
    """)
    query.exec("""
    CREATE TABLE IF NOT EXISTS clasificacion (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        equipo_id INTEGER NOT NULL UNIQUE,
        partidos_jugados INTEGER DEFAULT 0,
        partidos_ganados INTEGER DEFAULT 0,
        partidos_empatados INTEGER DEFAULT 0,
        partidos_perdidos INTEGER DEFAULT 0,
        goles_favor INTEGER DEFAULT 0,
        goles_contra INTEGER DEFAULT 0,
        diferencia_goles INTEGER DEFAULT 0,
        puntos INTEGER DEFAULT 0,
        FOREIGN KEY (equipo_id) REFERENCES equipos(id) ON DELETE CASCADE
    )
    """)
    print("Tablas creadas correctamente")
