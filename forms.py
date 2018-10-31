# forms.py

from wtforms import Form, StringField, SelectField, validators

class MosquitoSearchForm(Form):
    choices = [('Especie', 'Especie'),
               ('Nombre_cadena', 'Nombre_cadena'),
               ('Accesion', 'Accesion')]
    select = SelectField('Buscar informaciòn de especie:', choices=choices)
    search = StringField('')


class InfoForm(Form):
    cadena_types = [('Protein', 'Protein'),
                   ('Nucleotide', 'Nucleotide')
                   ]
    especie = StringField('Especie')
    nombre_cadena = StringField('Nombre_cadena')
    cadena = StringField('Cadena')
    accesion = StringField('Accesion')
    cadena_type = SelectField('Cadena', choices=cadena_types)
