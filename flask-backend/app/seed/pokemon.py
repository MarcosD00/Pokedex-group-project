
from app import app, db
from app.models import PokemonType, Item, Pokemon
from sqlalchemy.sql import text


def seed_pokemon():
    
   

    pokemon1 = Pokemon( number = 1, imageUrl= '/images/pokemon_snaps/1.svg', name= 'Bulbasaur', attack= 49, defense= 49, type= 'grass', moves= ['tackle','vine whip'], captured= True )
    pokemon2 = Pokemon(number= 2,
        imageUrl= '/images/pokemon_snaps/2.svg',
        name= 'Ivysaur',
        attack= 62,
        defense= 63,
        type= 'grass',
        moves= [
          'tackle',
          'vine whip',
          'razor leaf'
        ],
        captured= True)
    pokemon3 = Pokemon( number= 3,
        imageUrl= '/images/pokemon_snaps/3.svg',
        name= 'Venusaur',
        attack= 82,
        defense= 83,
        type= 'grass',
        moves= [
          'tackle',
          'vine whip',
          'razor leaf'
        ],
        captured= True)
    
    pokemon4 = Pokemon(number= 4,
        imageUrl= '/images/pokemon_snaps/4.svg',
        name= 'Charmander',
        attack= 52,
        defense= 43,
        type= 'fire',
        moves= [
          'scratch',
          'ember',
          'metal claw'
        ],
        captured= True)
    
    pokemon5 = Pokemon(number= 5,
        imageUrl= '/images/pokemon_snaps/5.svg',
        name= 'Charmeleon',
        attack= 64,
        defense= 58,
        type= 'fire',
        moves= [
          'scratch',
          'ember',
          'metal claw',
          'flamethrower'
        ],
        captured= True)
    lst_of_pokemons = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5]
    _= [db.session.add(poke) for poke in lst_of_pokemons]
    db.session.commit()

def undo_pokemon():
    db.session.execute(text("DELETE FROM users"))   
    db.session.commit()