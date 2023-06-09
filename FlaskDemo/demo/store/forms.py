from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length,DataRequired,Email,EqualTo, ValidationError

from store.models import User



class RegisterForm(FlaskForm):
    def validate_username(self,username_to_check):
        user=User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('User Name already exist..Please try another one..!')


    def validate_email(self,email_to_check):
        email_add=User.query.filter_by(email_address=email_to_check.data).first()
        if email_add:
            raise ValidationError('Email Address already exist..Please try another one..!')


    username=StringField(label='User Name',validators=[Length(min=4,max=15),DataRequired()])
    email=StringField(label='Email Address',validators=[Email(), DataRequired()])
    password1=PasswordField(label='Create Password',validators=[Length (min=6),DataRequired()])
    password2=PasswordField(label='Confirm Password' ,validators=[EqualTo('password1'),DataRequired()])
    submit=SubmitField(label='Create Account')



class LoginForm(FlaskForm):
   username=StringField(label='User Name',validators=[DataRequired()])
   password1=PasswordField(label='Create Password',validators=[DataRequired()])
   submit=SubmitField(label='Log In')


class PurchaseItem(FlaskForm):
    submit=SubmitField(label='Purchase item')   


class SellItem(FlaskForm):
    submit=SubmitField(label='Sell item')       