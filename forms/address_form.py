from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired


class AddressForm(FlaskForm):

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Surname', validators=[DataRequired()])
    country = SelectField('Country', choices=["UK", "US"])
    password = PasswordField('Password', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    town_city = StringField('Town/City', validators=[DataRequired()])
    postcode = StringField('Postcode', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    email_address = StringField('Email Address', validators=[DataRequired()])
    terms_and_conds = BooleanField('Terms and Conditions')


    submit = SubmitField('Create Account')
