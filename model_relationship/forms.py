from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField
from wtforms.validators import InputRequired




# class PostForm(FlaskForm):
#     title = StringField(label='Title', validators=[DataRequired()])
#     content = StringField(label='Content', validators=[DataRequired()])
#     submit = SubmitField('Submit')



class CommentForm(FlaskForm):
    content =TextAreaField(label='Comments',validators=[InputRequired()])
    submit = SubmitField('Submit')

