from flask import Flask, render_template, request, redirect
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
