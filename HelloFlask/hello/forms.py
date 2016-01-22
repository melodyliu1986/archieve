from flask.ext.wtf import Form
from wtforms import validators, StringField, SubmitField, TextAreaField


class CommentForm(Form):
    text = StringField('Comment', [validators.DataRequired()])
    multi_text = TextAreaField('Comment', [validators.DataRequired()])
    submit_button = SubmitField("Search")
