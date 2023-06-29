from flask.cli  import AppGroup
from .pokemon import seed_pokemon, undo_pokemon
from .item import seed_items, undo_items
# from .posts import seed_posts, undo_posts

seed_commands = AppGroup("seed")


@seed_commands.command("all")
def seed():
    # pokemon = seed_pokemon()
    seed_pokemon()
    seed_items()
    print("We will be seeding our DB")



@seed_commands.command("undo")
def undo():
    undo_pokemon()
    undo_items()
    # undo_users()
    print("We are destroying our data!")