# LevelUP Store

## Descripción

LevelUP Store es una tienda en línea de videojuegos construida con Django. Permite a los usuarios registrarse, navegar por una variedad de juegos, 
agregar productos al carrito y finalizar compras. Además, ofrece funcionalidades de autenticación, perfiles de usuario y una API REST para interactuar con los datos de la tienda.

## Características

- **Registro de usuarios**: Los usuarios pueden crear una cuenta en la tienda.
- **Login de usuarios**: Los usuarios pueden iniciar sesión y acceder a su perfil.
- **Gestión del perfil**: Los usuarios pueden editar su información personal.
- **Usuarios administrativos**: Los usuarios administrativos pueden editar, eliminar y agregar tanto perfiles como juegos
- **Lista de juegos**: Los usuarios pueden ver una lista de videojuegos con detalles como el nombre, la categoría, la descripción y el precio.
- **Carrito de compras**: Los usuarios pueden agregar juegos a su carrito y proceder con la compra.
- **API REST**: Se ofrece una API para obtener la lista de juegos, y de nombre de regiones
- **API REST** Se consumen dos API REST externas para filtrar juegos en promocion y trivia de video juegos
- **Seguridad**: Protege las vistas con autenticación mediante tokens para la API y tambien proteje las vistas que necesitan autenticacion y desglose de tipo de usuarios que puede acceder a ellas

## Instalación

Sigue estos pasos para instalar la aplicación en tu entorno local:

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/videojuegos_store.git
cd videojuegos_store

2. Crear y activar un entorno virtual
Si no tienes un entorno virtual creado, puedes crear uno usando venv:
python -m venv env
source env/bin/activate  # En Linux/macOS
env\Scripts\activate     # En Windows

3. Instalar las dependencias
Una vez activado el entorno virtual, instala las dependencias del proyecto:

bash
Copiar
Editar
pip install -r requirements.txt

4. Configuración de base de datos
Si estás usando una base de datos SQLite, puedes saltarte este paso. Si prefieres usar una base de datos diferente (por ejemplo, PostgreSQL), configura los ajustes de conexión en settings.py.

5. Ejecutar las migraciones
bash
Copiar
Editar
python manage.py migrate

6. Crear un superusuario (opcional)
Puedes crear un superusuario para acceder al panel de administración de Django:

bash
Copiar
Editar
python manage.py createsuperuser

7. Ejecutar el servidor
Inicia el servidor de desarrollo:

bash
Copiar
Editar
python manage.py runserver


Tecnologías utilizadas

Django 5.x

Django Rest Framework

SQL developer

Bootstrap 5

Python 3.x




