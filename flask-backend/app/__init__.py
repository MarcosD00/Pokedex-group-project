# import statement for CSRF
from flask import Flask, render_template, jsonify, request
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_migrate import Migrate
from .seed import seed_commands


import os
from .config import Configuration
from .models import db, Pokemon, Item, PokemonType
from .forms.pokemon_form import PokemonForm, ItemForm, PokemonTypeForm

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
Migrate(app, db)
app.cli.add_command(seed_commands)
# after request code for CSRF token injection


@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response


@app.route("/api/pokemon", methods=["GET"])
def index():
    pokemon = Pokemon.query.all()
    data = [{'id': poke.id, 'number': poke.number, 'attack': poke.attack, 'defense': poke.defense, 'imageUrl': poke.imageUrl, 'name': poke.name,
             'type': poke.type, 'moves': poke.moves, 'encounterRate': poke.encounterRate, 'catchRate': poke.catchRate, 'captured': poke.captured} for poke in pokemon]
    return jsonify(data)


@app.route('/api/pokemon', methods=['POST'])
def post_pokemon():
    form = PokemonForm()
    form2 = PokemonType()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        number = form.data["number"]
        attack = form.data["attack"]
        defense = form.data["defense"]
        imageUrl = form.data["imageUrl"]
        name = form.data["name"]
        type = form.data["type"]
        moves = f"{form.data['move1']}, {form.data['move2']}"
        encounterRate = form.data["encounterRate"]
        catchRate = form.data["catchRate"]
        captured = form.data["captured"]
        new_pokemon = Pokemon(numer=number, attack=attack,
                              defense=defense, imageUrl=imageUrl, name=name, type=type, moves=moves,
                              encounterRate=encounterRate, catchRate=catchRate, captured=captured)
        type = form.data["type"]
        new_type = PokemonType(type=type)
        db.session.add(new_pokemon)
        db.session.add(new_type)
        db.session.commit()
        print(form.data)
        return jsonify(new_pokemon, new_type)
    return jsonify(form.errors)
