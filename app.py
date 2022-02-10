from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

# Configuration of Database todo.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)


class Todotb(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300))
    complete = db.Column(db.Boolean)


@app.route('/' ,methods=['POST','GET'])
def index():
    
    incompleteit = Todotb.query.filter_by(complete=False).all()
    completeit = Todotb.query.filter_by(complete=True).all()
    if request.method == 'POST':
        q = request.form['q']
        searchtodo = Todotb.query.filter_by(text=q)
        return render_template('index.html', incompleteit=incompleteit, completeit=completeit,searchtodo=searchtodo)
    return render_template('index.html', incompleteit=incompleteit, completeit=completeit)

@app.route('/add', methods=['POST'])
def add():
    
    todo = Todotb(text=request.form['todotext'], complete=False)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('index'))



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)