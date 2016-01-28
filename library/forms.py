__author__ = 'liusong'

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField, validators


class SearchForm(Form):
    text = StringField("Search")
    submit_button = SubmitField("Search")


class AdvancedSearchForm(Form):
    book_name = StringField(label="Name:")
    book_cate = SelectField(label="Category:", choices=[('All Books', 'All Books'), ('Skill', 'Skill'), ('Management', 'Management'), ('Communication', 'Communication'), ('Leadership', 'Leadership'), ('Famous Person', 'Famous Person')])
    book_owner = StringField(label="Owner:")
    book_bought_time = StringField(label="Bought time:")
    submit_button = SubmitField("Submit")
