from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import func

app = Flask(__name__)

# Configuration of Database todo.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

# Table for to-do entries
class Todotb(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300))
    complete = db.Column(db.Boolean)


@app.route('/' ,methods=['POST','GET'])
def index():
    """_Main Page/Route for User interaction_
    Two Queries filtering by the complete status of to-do item.
    One Query for handling the search request 
    
    Returns:
        render_template function with the index.html file and the Queries as arguments
    """
    incompleteit = Todotb.query.filter_by(complete=False).all()
    completeit = Todotb.query.filter_by(complete=True).all()
    if request.method == 'POST':
        q = request.form['q']
        q_lower = q.lower()
        if not q_lower:
            return render_template('index.html', incompleteit=incompleteit, completeit=completeit)
        Todotb.text = func.lower(Todotb.text)
        searchtodo = Todotb.query.filter( Todotb.text.contains(q_lower)).all()
        return render_template('index.html', incompleteit=incompleteit, completeit=completeit,searchtodo=searchtodo)
    return render_template('index.html', incompleteit=incompleteit, completeit=completeit)

@app.route('/add', methods=['POST'])
def add():
    """_Route for adding to-do items to the database_
    Complete status of to-do items set to false since they cannot be completed if they just got recently added to the list.
        
    Returns:
        redirect to the main page/index.html
    """
    todo = Todotb(text=request.form['todotext'], complete=False)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/complete/<id>')
def complete(id):
    """_Route for setting the complete status of to-do items to True/completed_

    Args:
        id (_int_): _primary key of the to-do item being operated on_

    Returns:
        redirect to the main page/index.html
    """
    complete_todo = Todotb.query.filter_by(id=int(id)).first()
    complete_todo.complete = True
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
    """_Route for deleting to-do items_

    Args:
        id (_int_): _primary key of the to-do item being operated on_

    Returns:
        redirect to the main page/index.html
    """
    delete_todo = Todotb.query.filter_by(id=int(id)).first()
    db.session.delete(delete_todo)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)