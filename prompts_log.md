# Prompts Log - Examen Práctico 2
## Sistema de Gestión de Biblioteca Digital

Este archivo documenta el uso de IA durante el desarrollo del proyecto.  
Cada registro incluye el prompt utilizado, la respuesta obtenida, el código adoptado y las correcciones realizadas por el equipo.

---

## Prompt 1 - Estructura base del proyecto

**Tarea:** 3.1 Configuración del entorno extendido y continuidad del repositorio  
**LLM usada:** Antigravity  
**Integrante:** Yered Arana 
**Fecha/hora:** 15/05/2026  

### Prompt enviado:
Estoy ampliando el mismo Sistema de Gestión de Biblioteca Digital que ya tenía en Git. Necesito una propuesta de reorganización del repositorio para una versión con GUI, eventos, SQL, Mongo y workers en hilos. Dame la estructura de carpetas, comandos Git recomendados y criterios para repartir commits entre 4 integrantes.

### Respuesta resumida:
La IA propuso una estructura modular separando responsabilidades en carpetas como configuración, base de datos, modelos, servicios, interfaz gráfica, eventos, concurrencia y pruebas. También sugirió dividir el trabajo por integrantes para evitar conflictos.

### Código adoptado/modificado:
Se crearon las carpetas nuevas del examen 2:

- config/
- controllers/
- repositories/
- events/
- threads/
- ui/
- data/
- docs/

También se crearon los archivos:

- arquitectura.md
- prompts_log.md
- requirements.txt

### Qué corrigió el equipo:
Se adaptaron los nombres de carpetas a la estructura solicitada por el examen, usando `ui/`, `controllers/`, `repositories/`, `events/` y `threads/` en lugar de nombres diferentes como `gui/`, `db/` o `concurrencia/`.

### Tema del curso implementado:
Arquitectura modular, organización de proyecto, Git, trabajo colaborativo y preparación para programación orientada a eventos.

---

## Prompt 2 - Implementación de base de datos SQL y MongoDB

**Tarea:** 4.1 Base de datos relacional SQL y 4.2 Base de datos no relacional MongoDB  
**LLM usada:** Antigravity  
**Integrante:** Yered arana 
**Fecha/hora:** 15/05/2026  

### Prompt enviado:
Estoy trabajando en la parte de bases de datos del examen 2 de mi proyecto “Sistema de Gestión de Biblioteca Digital”.

Contexto:
Ya tengo un repositorio en GitHub con esta estructura:

modelos/
servicios/
utils/
tests/
config/
repositories/
data/
ui/
controllers/
events/
threads/
docs/
main.py
README.md
arquitectura.md
prompts_log.md
requirements.txt

Mi parte es implementar la persistencia híbrida:
- SQLite para datos relacionales/transaccionales.
- MongoDB para bitácora, auditoría o eventos del sistema.

NO quiero crear carpetas nuevas como db/ o datos/. Debo usar estas carpetas:
- config/
- repositories/
- data/

Necesito que me generes el contenido completo, ordenado y funcional para estos archivos:

1. config/settings.py
2. repositories/sql_connection.py
3. repositories/libro_repository.py
4. repositories/usuario_repository.py
5. repositories/prestamo_repository.py
6. repositories/mongo_repository.py

Requisitos:
- Usar SQLite con la base en data/biblioteca.db.
- Crear automáticamente las tablas si no existen.
- Tablas necesarias: libros, usuarios y prestamos.
- Usar consultas parametrizadas con ? para evitar SQL Injection.
- Activar FOREIGN KEY en SQLite.
- Incluir CRUD completo para libros.
- Incluir CRUD básico para usuarios.
- Incluir registrar préstamo y devolver préstamo.
- Cuando se registra un préstamo, el libro debe quedar como no disponible.
- Cuando se devuelve un préstamo, el libro debe quedar disponible.
- Incluir manejo de errores con try/except específicos usando sqlite3.Error.
- El código debe tener type hints y docstrings.
- Debe ser entendible para estudiantes, no excesivamente avanzado.
- Debe poder ser llamado después desde la GUI y controladores.
- No uses SQLAlchemy, solo sqlite3 nativo de Python.
- Para MongoDB usa pymongo, pero agrega manejo de error si Mongo no está disponible.
- Mongo debe tener una función registrar_evento(tipo, descripcion, datos=None) para guardar bitácora.
- Si Mongo falla, el sistema no debe romperse.

Campos sugeridos:

Tabla libros:
id, titulo, autor, isbn, anio, genero, tipo, disponible

Tabla usuarios:
id, nombre, email, rol, limite_libros

Tabla prestamos:
id, usuario_id, libro_id, fecha_prestamo, fecha_devolucion, activo

Además:
- Dame también un pequeño bloque de prueba temporal para main.py que inicialice la base, inserte datos demo, liste libros y pruebe un préstamo.
- Explícame brevemente qué hace cada archivo.
- No mezcles la interfaz gráfica todavía. Solo quiero la capa de base de datos lista.

### Respuesta resumida:
La IA propuso implementar una capa de repositorios usando SQLite para libros, usuarios y préstamos, además de MongoDB para registrar eventos del sistema. También propuso crear una configuración centralizada en `config/settings.py` y separar las operaciones en archivos independientes dentro de `repositories/`.

### Código adoptado/modificado:
Se implementaron o actualizaron los siguientes archivos:

- config/settings.py
- repositories/sql_connection.py
- repositories/libro_repository.py
- repositories/usuario_repository.py
- repositories/prestamo_repository.py
- repositories/mongo_repository.py

Se creó la base de datos:

- data/biblioteca.db

### Qué corrigió el equipo:
Se adaptó el código a la estructura real del repositorio.  
Se verificó que no se usaran carpetas nuevas como `db/` o `datos/`.  
Se corrigió el repositorio de préstamos para incluir correctamente las funciones `registrar_prestamo()` y `devolver_prestamo()`.  
Se corrigió el repositorio de MongoDB para incluir la función `registrar_evento()` y evitar que el sistema se cierre si MongoDB no está disponible.

### Pruebas realizadas:
Se probó desde la terminal de Python que:

- La base `data/biblioteca.db` se crea correctamente.
- Existen las tablas `libros`, `usuarios` y `prestamos`.
- Se puede crear un libro.
- Se puede crear un usuario.
- Se puede registrar un préstamo.
- Al prestar un libro, su disponibilidad cambia de `1` a `0`.
- Se puede devolver un préstamo.
- Al devolver el libro, su disponibilidad cambia de `0` a `1`.
- MongoDB puede registrar o ignorar eventos sin romper el sistema.

### Tema del curso implementado:
Base de datos SQL, SQLite, MongoDB, CRUD, consultas parametrizadas, llaves foráneas, manejo de excepciones, persistencia híbrida y arquitectura modular.

---

## Prompt 3 - Corrección de errores durante pruebas de base de datos

**Tarea:** 4.1 SQL, 4.2 MongoDB y 4.4 CRUD con Python  
**LLM usada:** Antigravity  
**Integrante:** Yered Arana  
**Fecha/hora:** 15/05/2026  

### Prompt enviado:
Durante las pruebas del módulo de base de datos, aparecieron errores al importar funciones desde `repositories/`, al abrir `data/biblioteca.db` y al devolver préstamos. Necesito ayuda para identificar si estoy en la carpeta correcta, revisar las tablas y probar las funciones de préstamo y devolución.

### Respuesta resumida:
La IA explicó que algunos errores se debían a estar ubicada en la carpeta incorrecta del proyecto y otros a funciones que no existían con el nombre esperado. También indicó cómo revisar las tablas de SQLite y cómo identificar el ID correcto de un préstamo activo.

### Código adoptado/modificado:
Se ajustó el archivo `prestamo_repository.py` para incluir correctamente:

- registrar_prestamo()
- devolver_prestamo()

También se revisó `mongo_repository.py` para incluir:

- registrar_evento()

### Qué corrigió el equipo:
Se comprobó que el proyecto debía ejecutarse desde la carpeta donde se encuentran `main.py`, `repositories/`, `config/` y `data/`.  
Se verificó que el préstamo activo tenía un ID diferente al esperado, por lo que se usó el ID correcto para devolver el libro.

### Tema del curso implementado:
Depuración, manejo de errores, pruebas manuales, base de datos SQLite, CRUD y control de disponibilidad de libros.E
