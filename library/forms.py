__author__ = 'liusong'

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, validators


class SearchForm(Form):
    text = StringField("Search", validators=[validators.DataRequired()])
    submit_button = SubmitField("Search")

