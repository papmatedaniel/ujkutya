"""from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///allatok.db'
db = SQLAlchemy(app)

class Allat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nev = db.Column(db.String(80), nullable=False)
    nem = db.Column(db.String(10), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/allat_hozzaadasa', methods=['POST'])
def allat_hozzaadasa():
    nev = request.form['nev']
    nem = request.form['nem']
    uj_allat = Allat(nev=nev, nem=nem)
    db.session.add(uj_allat)
    db.session.commit()
    return redirect('/')


@app.route('/allatmodositasa')
def allatmodositasa():
    allatok = Allat.query.all()
    return render_template('allatmodositasa.html', allatok=allatok)

@app.route('/allat_frissitese', methods=['POST'])
def allat_frissitese():
    for allat in Allat.query.all():
        allat_id = allat.id
        if f"update_{allat_id}" in request.form['action']:
            allat.nev = request.form[f'nev{allat_id}']
            allat.nem = request.form[f'nem{allat_id}']
        elif f"delete_{allat_id}" in request.form['action']:
            db.session.delete(allat)
    if "update_all" in request.form['action']:
        for allat in Allat.query.all():
            allat.nev = request.form[f'nev{allat.id}']
            allat.nem = request.form[f'nem{allat.id}']
    db.session.commit()
    return redirect('/tablazat')





@app.route('/tablazat')
def tablazat():
    users = Allat.query.all()
    return render_template('tablazat.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
"""

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///allatok.db'
db = SQLAlchemy(app)

class Allat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nev = db.Column(db.String(80), nullable=False)
    nem = db.Column(db.String(10), nullable=False)
    csipszam = db.Column(db.Integer)
    fajta = db.Column(db.String(100))
    tipus = db.Column(db.String(100))
    egeszsegiallapot = db.Column(db.String(100))
    fogazat = db.Column(db.String(50))
    kor = db.Column(db.Integer)
    viselkedes = db.Column(db.String(200))
    egyeb = db.Column(db.String(200))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/allat_hozzaadasa', methods=['POST'])
def allat_hozzaadasa():
    nev = request.form['nev']
    nem = request.form['nem']
    csipszam = request.form['csipszam']
    fajta = request.form['fajta']
    tipus = request.form['tipus']
    egeszsegiallapot = request.form['egeszsegiallapot']
    fogazat = request.form['fogazat']
    kor = request.form['kor']
    viselkedes = request.form['viselkedes']
    egyeb = request.form['egyeb']
    
    uj_allat = Allat(nev=nev, nem=nem, csipszam=csipszam, fajta=fajta, tipus=tipus, egeszsegiallapot=egeszsegiallapot, fogazat=fogazat, kor=kor, viselkedes=viselkedes, egyeb=egyeb)
    db.session.add(uj_allat)
    db.session.commit()
    return redirect('/')

@app.route('/allatmodositasa')
def allatmodositasa():
    allatok = Allat.query.all()
    return render_template('allatmodositasa.html', allatok=allatok)

@app.route('/allat_frissitese', methods=['POST'])
def allat_frissitese():
    for allat in Allat.query.all():
        allat_id = allat.id
        if f"update_{allat_id}" in request.form['action']:
            allat.nev = request.form[f'nev{allat_id}']
            allat.nem = request.form[f'nem{allat_id}']
            allat.csipszam = request.form[f'csipszam{allat_id}']
            allat.fajta = request.form[f'fajta{allat_id}']
            allat.tipus = request.form[f'tipus{allat_id}']
            allat.egeszsegiallapot = request.form[f'egeszsegiallapot{allat_id}']
            allat.fogazat = request.form[f'fogazat{allat_id}']
            allat.kor = request.form[f'kor{allat_id}']
            allat.viselkedes = request.form[f'viselkedes{allat_id}']
            allat.egyeb = request.form[f'egyeb{allat_id}']
        elif f"delete_{allat_id}" in request.form['action']:
            db.session.delete(allat)
    if "update_all" in request.form['action']:
        for allat in Allat.query.all():
            allat.nev = request.form[f'nev{allat.id}']
            allat.nem = request.form[f'nem{allat.id}']
            allat.csipszam = request.form[f'csipszam{allat.id}']
            allat.fajta = request.form[f'fajta{allat.id}']
            allat.tipus = request.form[f'tipus{allat.id}']
            allat.egeszsegiallapot = request.form[f'egeszsegiallapot{allat.id}']
            allat.fogazat = request.form[f'fogazat{allat.id}']
            allat.kor = request.form[f'kor{allat.id}']
            allat.viselkedes = request.form[f'viselkedes{allat.id}']
            allat.egyeb = request.form[f'egyeb{allat.id}']
    db.session.commit()
    return redirect('/tablazat')

@app.route('/tablazat')
def tablazat():
    users = Allat.query.all()
    return render_template('tablazat.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
