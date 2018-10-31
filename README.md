# BC-project
<ul>
BC-flask python
<li>Desarrollar el programa en un entorno virtual de python: </li>
<ul>
<li> descargar: sudo apt-get install python-virtualenv virtualenv </li>
<li> crear entorno virtual: virtualenv --python=python3 .venv //recomiendo crearlo en una carpeta del home con nombre Entornos </li>
<li> // Dentro de Entornos activamos  </li>
<li> activar entorno: source .venv/bin/activate</li>
</ul>
<li> Un vez dentro del entorno virtual descargamos las librerias y podemos desplazarnos la carpeta donde se encuetra el proyecto, el orden no importa siempre y cuando estemos dentro del entorno virtual</li>
<ul>
<li> Flask: pip3 install flask </li>
<li> SQLAlchemy: pip install flask-sqlalchemy  </li>
<li> Flask-WTF: pip install Flask-WTF  </li>
<li> Flask Tables: pip install flask_table</li>
</ul>
<li> correr app: FLASK_APP=main.py flask run </li>
<li> opcional: Enviroment: export FLASK_ENV=True </li> 
</ul>
