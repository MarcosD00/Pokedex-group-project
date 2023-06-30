from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, FloatField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

poke_type = [
    "fire",
    "electric",
    "normal",
    "ghost",
    "psychic",
    "water",
    "bug",
    "dragon",
    "grass",
    "fighting",
    "ice",
    "flying",
    "poison",
    "ground",
    "rock",
    "steel",
]


class PokemonForm(FlaskForm):
    number = IntegerField("Number", validators=[DataRequired()])
    attack = IntegerField("Attack", validators=[DataRequired()])
    defense = IntegerField("Defense", validators=[DataRequired()])
    imageUrl = StringField("Image Url", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    type = SelectField("Type", validators=[DataRequired()], choices=poke_type)
    moves = StringField("Moves")
    encounterRate = FloatField("Encounter Rate")
    catchRate = FloatField("Catch Rate")
    captured = BooleanField("Captured", validators=[DataRequired()])
    submit = SubmitField("Submit")


class ItemForm(FlaskForm):
    happiness = IntegerField("Happiness", validators=[DataRequired()])
    imageUrl = StringField("Image Url", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    price = IntegerField("Price", validators=[DataRequired()])
    pokemonId = IntegerField("Number", validators=[DataRequired()])
    submit = SubmitField("Submit")


choices = [('other', 'Other'), ('string', 'String'), ('woodwind',
                                                      'Woodwind'), ('brass', 'Brass'), ('percussion', 'Percussion')]


class PokemonTypeForm(FlaskForm):
    types = SelectField("Types", choices=choices)
