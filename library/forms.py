__author__ = 'liusong'

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, validators


class SearchForm(Form):
    text = StringField("Search", validators=[validators.DataRequired()])
    submit_button = SubmitField("Search")


class AdvancedSearchForm(Form):
    book_name = StringField(label="Name:")
    book_cate = StringField(label="Category:")
    book_owner = StringField(label="Owner:")
    book_bought_time = StringField(label="Bought time:")
    submit_button = SubmitField("Submit")


