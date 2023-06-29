from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

types = [
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


class Pokemon(db.Model):
    __tablename__ = "Pokemons"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), nullable=False)
    moves = db.Column(db.String(255), nullable=False)
    encounterRate = db.Column(db.Float(3, 2))
    catchRate = db.Column(db.Float(3, 2))
    captured = db.Column(db.Boolean)
    item_poke = db.relationship("Item", back_populates='poke_item')


class Item(db.Model):
    __tablename__ = 'Items'
    id = db.Column(db.Integer, primary_key=True)
    happiness = db.Column(db.Integer)
    imageUrl = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    pokemonId = db.Column(db.Integer, db.ForeignKey(
        'Pokemons.id'), nullable=False)
    poke_item = db.relationship("Pokemon", back_populates='item_poke')


class PokemonType(db.Model):
    __tablename__ = 'PokemonTypes'
    id = db.Column(db.Integer, primary_key=True)
    types = db.Column(db.String)
