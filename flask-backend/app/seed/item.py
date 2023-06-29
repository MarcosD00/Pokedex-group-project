# from app import app
from app.models import PokemonType, Item, Pokemon, db
from sqlalchemy.sql import text


def seed_items():

    item1 = Item(happiness = 50, imageUrl = '/images/pokemon_snaps/1.svg', name = 'pokemon_potion', price = 99, pokemonId=1) 


    lst_of_items = [item1]
    _= [db.session.add(item) for item in lst_of_items]
    db.session.commit()

def undo_items():
    db.session.execute(text("DELETE FROM items"))   
    db.session.commit()