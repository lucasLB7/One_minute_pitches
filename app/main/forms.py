
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField
from wtforms.validators import Required

class CommentsForm(FlaskForm):
    comment = TextAreaField('What do you think about this pitch?', validators=[Required()])
    vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])
    submit = SubmitField('SUBMIT')  

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit') 

class PitchForm(FlaskForm):
    category_id = SelectField('Select Category', choices=[('1', 'Creative Ideas'), ('2', 'Funny Stories'), ('3', 'Motivational speeches'),('4','Business ideas')])
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('Create Pitch')

class UpvoteForm(FlaskForm):

    submit = SubmitField('Upvote')
    