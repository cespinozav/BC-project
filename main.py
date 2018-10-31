# main.py

from app import app
from db_setup import init_db, db_session
from forms import MosquitoSearchForm, InfoForm
from flask import flash, render_template, request, redirect
from models import Info, Especie
from tables import Results

init_db()


@app.route('/', methods=['GET', 'POST'])
def index():
    search = MosquitoSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)


@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search_string:
        if search.data['select'] == 'Especie':
            qry = db_session.query(Info, Especie).filter(
                Especie.id==Info.especie_id).filter(
                    Especie.name.contains(search_string))
            results = [item[0] for item in qry.all()]
        elif search.data['select'] == 'Info':
            qry = db_session.query(Info).filter(
                Info.nombre_cadena.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Accesion':
            qry = db_session.query(Info).filter(
                Info.accesion.contains(search_string))
            results = qry.all()
        else:
            qry = db_session.query(Info)
            results = qry.all()
    else:
        qry = db_session.query(Info)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        print(results)

        table.border = True
        return render_template('results.html', table=table)


@app.route('/new_album', methods=['GET', 'POST'])
def new_album():
    """
    Add a new info
    """
    form = InfoForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the info
        info = Info()
        save_changes(info, form, new=True)
        flash('info created successfully!')
        return redirect('/')

    return render_template('new_album.html', form=form)


def save_changes(info, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    especie = Especie()
    especie.name = form.especie.data

    info.especie = especie
    info.nombre_cadena = form.nombre_cadena.data
    info.cadena = form.cadena.data
    info.accesion = form.accesion.data
    info.cadena_type = form.cadena_type.data
    print (info.cadena)
    if new:
        # Add the new info to the database
        db_session.add(info)

    # commit the data to the database
    db_session.commit()


@app.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    """
    Add / edit an item in the database
    """
    qry = db_session.query(Info).filter(
                Info.id==id)
    info = qry.first()

    if info:
        form = InfoForm(formdata=request.form, obj=info)
        if request.method == 'POST' and form.validate():
            # save edits
            save_changes(info, form)
            flash('info updated successfully!')
            return redirect('/')
        return render_template('edit_album.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    """
    Delete the item in the database that matches the specified
    id in the URL
    """
    qry = db_session.query(Info).filter(Info.id==id)
    info = qry.first()

    if info:
        form = InfoForm(formdata=request.form, obj=info)
        if request.method == 'POST' and form.validate():
            # delete the item from the database
            db_session.delete(info)
            db_session.commit()

            flash('info deleted successfully!')
            return redirect('/')
        return render_template('delete_album.html', form=form)
    else:
        return 'Error deleting #{id}'.format(id=id)


if __name__ == '__main__':
    import os
    if 'WINGDB_ACTIVE' in os.environ:
        app.debug = False
    app.run(port=5001)