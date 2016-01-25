import os
import sqlite3
from flask import g, Flask, render_template, flash, redirect, url_for, request


import forms

DATABASE = '{0}/database/book_owner.db'.format(os.getcwd())
DEBUG = True

app = Flask(__name__)


def connect_db():
    return sqlite3.connect(DATABASE)


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


@app.route('/', methods=['GET', 'POST'])
def main_page():
    search_form = forms.SearchForm(csrf_enabled=False)
    if search_form.validate_on_submit():
        search_data = search_form.text.data
        db = connect_db()
        search_str = 'select * from book_owner where book like "%{0}%";'.format(search_data)
        items = db.execute(search_str).fetchall()
        if len(items) == 0:
            return render_template("no_result.html")
        else:
            return render_template("result.html", items=items)
    return render_template("main_page.html", search_form=search_form)


@app.route('/all_books')
def all_books():
    db = connect_db()
    items = db.execute("select * from book_owner;").fetchall()
    len_items = len(items)
    print "*"*20
    print items
    print len(items)
    return render_template("show_books.html", items=items, len_items=len_items)


@app.route('/book_category')
def book_category():
    db = connect_db()
    time1_select_str = 'select * from book_owner where buytime like "%{0}%";'.format("Before")
    time1_items = db.execute(time1_select_str).fetchall()

    time2_select_str = 'select * from book_owner where buytime like "%{0}%";'.format("FY15")
    time2_items = db.execute(time2_select_str).fetchall()

    time3_select_str = 'select * from book_owner where buytime like "%{0}%";'.format("FY16")
    time3_items = db.execute(time3_select_str).fetchall()

    # Select by category.
    skill_select_str = 'select * from book_owner where category like "%{0}%";'.format("Skill")
    skill_items = db.execute(skill_select_str).fetchall()

    management_select_str = 'select * from book_owner where category like "%{0}%";'.format("Management")
    management_items = db.execute(management_select_str).fetchall()

    leadership_select_str = 'select * from book_owner where category like "%{0}%";'.format("Leadership")
    leadership_items = db.execute(leadership_select_str).fetchall()

    famous_person_select_str = 'select * from book_owner where category like "%{0}%";'.format("Famous")
    famous_person_items = db.execute(famous_person_select_str).fetchall()

    return render_template("book_categories.html",
                           time1_items=time1_items,
                           time2_items=time2_items,
                           time3_items=time3_items,
                           skill_items=skill_items,
                           management_items=management_items,
                           leadership_items=leadership_items,
                           famous_person_items=famous_person_items)


@app.route('/search')
def search(data):
    db = connect_db()
    search_str = 'select * from book_owner where book like "%{0}%";'.format(data)
    items = db.execute(search_str).fetchall()
    if len(items) == 0:
        return render_template("no_result.html")
    else:
        return render_template("result.html", items=items)


@app.route('/no_result')
def search_no_result():
    db = connect_db()
    search_str = 'select * from book_owner where book like "%{0}%";'.format("L11111")
    items = db.execute(search_str).fetchall()
    if len(items) == 0:
        return render_template("no_result.html")
    else:
        return render_template("result.html", items=items)


if __name__ == "__main__":
    app.run(debug=True)
