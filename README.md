# BC-project
BC-flask python
Desarrollar el programa en un entorno virtual de python:
descargar: sudo apt-get install python-virtualenv virtualenv
crear entorno virtual: virtualenv --python=python3 .venv //recomiendo crearlo en una carpeta del home con nombre Entornos
// Dentro de Entornos activamos 
activar entorno: source .venv/bin/activate
Un vez dentro del entorno virtual descargamos las librerias.
Flask: pip3 install flask
SQLAlchemy: pip install flask-sqlalchemy
Flask-WTF: pip install Flask-WTF
Flask Tables: pip install flask_table

correr app: FLASK_APP=main.py flask run

opcional: Enviroment: export FLASK_ENV=True  
<ul>
<li>Line 1</li>
<li>Line 2</li>
</ul>
