import os
import sqlite3
from flask import g, Flask, render_template, flash, redirect, url_for

DATABASE = '{0}/database/book_owner.db'.format(os.getcwd())
DEBUG = True

app = Flask(__name__)


def connect_db():
    return sqlite3.connect(DATABASE)

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/')
def main_page():
    return render_template("main_page.html")

@app.route('/all_books')
def all_books():
    db = connect_db()
    items = db.execute("select * from book_owner;").fetchall()
    print items
    return render_template("show_books.html", items=items)

if __name__ == "__main__":
    app.run()
