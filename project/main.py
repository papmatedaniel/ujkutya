from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(10), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    gender = request.form['gender']
    new_user = User(name=name, gender=gender)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/')


@app.route('/felhasznalomodositasa')
def felhasznalomodositasa():
    users = User.query.all()
    return render_template('felhasznalomodositasa.html', users=users)

@app.route('/update_user', methods=['POST'])
def update_user():
    for user in User.query.all():
        user_id = user.id
        if f"update_{user_id}" in request.form['action']:
            user.name = request.form[f'name{user_id}']
            user.gender = request.form[f'gender{user_id}']
        elif f"delete_{user_id}" in request.form['action']:
            db.session.delete(user)
    if "update_all" in request.form['action']:
        for user in User.query.all():
            user.name = request.form[f'name{user.id}']
            user.gender = request.form[f'gender{user.id}']
    db.session.commit()
    return redirect('/table')





@app.route('/table')
def table():
    users = User.query.all()
    return render_template('table.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
