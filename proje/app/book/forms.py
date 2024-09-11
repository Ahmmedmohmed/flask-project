from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from flask_wtf.file import FileField, FileAllowed  
from wtforms.validators import DataRequired, Length,NumberRange



class bookform(FlaskForm):
 

    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=100)])
    image= FileField('Cover Photo', validators=[FileAllowed(['jpg', 'png'])])
    pages = IntegerField('Number of Pages', validators=[DataRequired(), NumberRange(min=1)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Create Book')