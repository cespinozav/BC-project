from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    especie = Col('Especie')
    nombre_cadena = Col('NombreCadena')
    cadena = Col('Cadena')
    accesion = Col('Accesion')
    cadena_type = Col('TypeCadena')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))