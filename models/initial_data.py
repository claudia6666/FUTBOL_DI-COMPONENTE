from PySide6.QtSql import QSqlQuery
def insertar_datos_iniciales(db):
    query = QSqlQuery(db)
    query.exec("SELECT COUNT(*) FROM equipos")
    if query.next() and query.value(0) > 0:
        print("La base de datos ya contiene datos")
        return
    print("Insertando datos iniciales...")
    equipos = [
        ("Los Tigres", "1º ESO A", "255,165,0"),
        ("Águilas FC", "1º ESO B", "0,0,255"),
        ("Leones Dorados", "2º ESO A", "255,255,0"),
        ("Panteras Negras", "2º ESO B", "0,0,0"),
        ("Dragones Rojos", "3º ESO A", "255,0,0"),
        ("Halcones Azules", "3º ESO B", "135,206,235"),
        ("Lobos Grises", "4º ESO A", "128,128,128"),
        ("Fénix Dorado", "4º ESO B", "255,215,0"),
    ]
    for equipo in equipos:
        query.prepare("""
            INSERT INTO equipos (nombre, curso, color_camiseta)
            VALUES (?, ?, ?)
        """)
        query.addBindValue(equipo[0])
        query.addBindValue(equipo[1])
        query.addBindValue(equipo[2])
        query.exec()
    print("Equipos insertados")
    arbitros = [
        ("Carlos Martínez", "1985-03-15", None, "Arbitro"),
        ("Laura Sánchez", "1990-07-22", None, "Arbitro"),
        ("Miguel Rodríguez", "1988-11-08", None, "Arbitro"),
        ("Ana García", "1992-05-30", None, "Arbitro"),
    ]
    for arbitro in arbitros:
        query.prepare("""
            INSERT INTO participantes (nombre, fecha_nacimiento, curso, tipo_participante)
            VALUES (?, ?, ?, ?)
        """)
        query.addBindValue(arbitro[0])
        query.addBindValue(arbitro[1])
        query.addBindValue(arbitro[2])
        query.addBindValue(arbitro[3])
        query.exec()
    print("Arbitros insertados")
    jugadores_tigres = [
        ("Diego Fernández", "2009-01-15", "1º ESO A", "Jugador", "Delantero", 1),
        ("Lucas Pérez", "2009-03-22", "1º ESO A", "Jugador", "Centrocampista", 1),
        ("Mario Gómez", "2009-05-10", "1º ESO A", "Jugador", "Defensa", 1),
        ("Pablo Torres", "2009-02-28", "1º ESO A", "Jugador", "Portero", 1),
    ]
    jugadores_aguilas = [
        ("Javier Ruiz", "2009-04-12", "1º ESO B", "Jugador", "Delantero", 2),
        ("Alberto Díaz", "2009-06-18", "1º ESO B", "Jugador", "Centrocampista", 2),
        ("Sergio Morales", "2009-08-05", "1º ESO B", "Jugador", "Defensa", 2),
        ("Raúl Castro", "2009-07-14", "1º ESO B", "Jugador", "Portero", 2),
    ]
    jugadores_leones = [
        ("Antonio López", "2008-09-20", "2º ESO A", "Jugador", "Delantero", 3),
        ("Fernando Vega", "2008-11-30", "2º ESO A", "Jugador", "Centrocampista", 3),
        ("Ricardo Jiménez", "2008-12-25", "2º ESO A", "Jugador", "Defensa", 3),
        ("Manuel Ortiz", "2008-10-08", "2º ESO A", "Jugador", "Portero", 3),
    ]
    jugadores_panteras = [
        ("David Navarro", "2008-02-14", "2º ESO B", "Jugador", "Delantero", 4),
        ("Marcos Herrera", "2008-04-21", "2º ESO B", "Jugador", "Centrocampista", 4),
        ("Adrián Romero", "2008-06-17", "2º ESO B", "Jugador", "Defensa", 4),
        ("Iván Molina", "2008-03-09", "2º ESO B", "Jugador", "Portero", 4),
    ]
    jugadores_dragones = [
        ("Cristian Gutiérrez", "2007-07-25", "3º ESO A", "Jugador", "Delantero", 5),
        ("Pablo Sánchez", "2007-09-12", "3º ESO A", "Jugador", "Centrocampista", 5),
        ("Ángel Medina", "2007-10-30", "3º ESO A", "Jugador", "Defensa", 5),
        ("Roberto Flores", "2007-08-19", "3º ESO A", "Jugador", "Portero", 5),
    ]
    jugadores_halcones = [
        ("Víctor Silva", "2007-01-08", "3º ESO B", "Jugador", "Delantero", 6),
        ("Guillermo López", "2007-02-18", "3º ESO B", "Jugador", "Centrocampista", 6),
        ("Enrique Martín", "2007-03-25", "3º ESO B", "Jugador", "Defensa", 6),
        ("Javier Ramos", "2007-04-14", "3º ESO B", "Jugador", "Portero", 6),
    ]
    jugadores_lobos = [
        ("Eduardo Campos", "2006-05-11", "4º ESO A", "Jugador", "Delantero", 7),
        ("Andrés Ponce", "2006-06-22", "4º ESO A", "Jugador", "Centrocampista", 7),
        ("Felipe Vargas", "2006-07-30", "4º ESO A", "Jugador", "Defensa", 7),
        ("Tomás Navarro", "2006-08-12", "4º ESO A", "Jugador", "Portero", 7),
    ]
    jugadores_fenix = [
        ("Carlos Vélez", "2006-09-20", "4º ESO B", "Jugador", "Delantero", 8),
        ("Nicolás Robles", "2006-10-28", "4º ESO B", "Jugador", "Centrocampista", 8),
        ("Santiago Rivera", "2006-11-15", "4º ESO B", "Jugador", "Defensa", 8),
        ("Gonzalo Peña", "2006-12-05", "4º ESO B", "Jugador", "Portero", 8),
    ]
    todos_jugadores = (jugadores_tigres + jugadores_aguilas + jugadores_leones + 
                       jugadores_panteras + jugadores_dragones + jugadores_halcones + 
                       jugadores_lobos + jugadores_fenix)
    for jugador in todos_jugadores:
        query.prepare("""
            INSERT INTO participantes (nombre, fecha_nacimiento, curso, tipo_participante, posicion, equipo_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """)
        query.addBindValue(jugador[0])
        query.addBindValue(jugador[1])
        query.addBindValue(jugador[2])
        query.addBindValue(jugador[3])
        query.addBindValue(jugador[4])
        query.addBindValue(jugador[5])
        query.exec()
    print("Jugadores insertados")
    partidos = [
        (1, 2, 1, 0, 0, "2025-02-15", "16:00", "Octavos", "Programado"),
        (3, 4, 2, 0, 0, "2025-02-15", "17:30", "Octavos", "Programado"),
        (5, 6, 3, 0, 0, "2025-02-16", "16:00", "Octavos", "Programado"),
        (7, 8, 4, 0, 0, "2025-02-16", "17:30", "Octavos", "Programado"),
        (1, 3, 1, 0, 0, "2025-02-22", "16:00", "Cuartos", "Programado"),
        (5, 7, 2, 0, 0, "2025-02-22", "17:30", "Cuartos", "Programado"),
        (1, 5, 3, 0, 0, "2025-03-01", "16:00", "Semifinal", "Programado"),
        (2, 6, 4, 0, 0, "2025-03-01", "17:30", "Semifinal", "Programado"),
        (1, 2, 1, 0, 0, "2025-03-15", "18:00", "Final", "Programado"),
    ]
    for partido in partidos:
        query.prepare("""
            INSERT INTO partidos (equipo1_id, equipo2_id, arbitro_id, goles_equipo1, 
                                 goles_equipo2, fecha, hora, ronda, estado)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """)
        query.addBindValue(partido[0])
        query.addBindValue(partido[1])
        query.addBindValue(partido[2])
        query.addBindValue(partido[3])
        query.addBindValue(partido[4])
        query.addBindValue(partido[5])
        query.addBindValue(partido[6])
        query.addBindValue(partido[7])
        query.addBindValue(partido[8])
        if query.exec():
            print(f"✓ Partido insertado: {partido}")
        else:
            print(f"✗ Error: {query.lastError().text()}")
    print("Partidos predefinidos insertados")
    query.exec("SELECT id FROM equipos")
    while query.next():
        equipo_id = query.value(0)
        query_clasificacion = QSqlQuery(db)
        query_clasificacion.prepare("""
            INSERT INTO clasificacion (equipo_id, partidos_jugados, partidos_ganados, 
                                      partidos_empatados, partidos_perdidos, goles_favor, 
                                      goles_contra, diferencia_goles, puntos)
            VALUES (?, 0, 0, 0, 0, 0, 0, 0, 0)
        """)
        query_clasificacion.addBindValue(equipo_id)
        query_clasificacion.exec()
    print("Clasificación inicial creada")
    print("✓ Datos iniciales insertados correctamente")
