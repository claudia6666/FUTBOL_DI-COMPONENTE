Gestor de Torneos de Fútbol

Bueno, aquí está mi aplicación para gestionar torneos de fútbol. Es una interfaz gráfica hecha con PySide6 que te permite llevar un control completo de equipos, partidos, resultados y todo ese rollo.

¿Qué puedes hacer?

- Equipos: Crear equipos, asignar jugadores, arbitros, todo eso
- Partidos: Programar partidos, ver calendarios, asignar árbitros
- Resultados: Meter goles y tarjetas, llevar un registro de todo
- Participantes: Gestionar jugadores y árbitros de la base de datos
- Tablas y Eliminatorias: Ver clasificaciones y bracket de eliminatorias
- Búsqueda y Filtros: Puedes filtrar por equipo, fecha, estado, lo que necesites

Instalación

Si quieres ejecutar el .exe directamente
Simplemente abre dist/main.exe y listo. No necesitas nada más.

Si quieres ejecutar desde código (desarrollo)

1. Copia el proyecto
2. Crea un entorno virtual:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install PySide6
```

4. Ejecuta:
```bash
python main.py
```

Base de datos

La app usa SQLite. La base de datos se crea automáticamente la primera vez que ejecutas la aplicación. Las tablas son:
- `equipos`
- `participantes` (jugadores y árbitros)
- `partidos`
- `resultados` (goles y tarjetas)

Si necesitas resetear la BD, simplemente borra `futbol.db` y se recreará.

Estructura del proyecto

Futbol_DI/
├── main.py                 # El punto de entrada
├── models/                 # Base de datos y conexiones
│   ├── database.py
│   ├── globals.py
│   └── initial_data.py
├── views/                  # Las vistas/pantallas
│   ├── mainWindow.py
│   ├── form_partido.py
│   ├── form_resultado.py
│   └── ...más vistas
├── widgets/                # Los archivos UI compilados a Python
├── ui/                     # Archivos .ui de Qt Designer
└── resources/              # Imágenes y assets
    └── img/


Nuevas integraciones 
Hemos integrado de forma modular un proyecto sobre un reloj digital. En este proyecto de futbol he creado un apartado de gestion de partidos con 2 modos:
    - Modo futbol: puedes gestionar los partidos en tiempo real con un temporizados y añadir goles/tarjetas en el equipo, con el jugador y el minuto exacto.

    -Modo reloj: un reloj/temporizador/cronometro que se puede poner en 12 o 24 horas y activar alarmas.

