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


@app.route("/")
def index():
  return render_template('index.html')



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)