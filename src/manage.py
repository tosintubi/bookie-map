import click
from flask.cli import with_appcontext

from src import db
from bootstrap.seeder import seed_data


# Custom commands to manage migrations
# https://flask.palletsprojects.com/en/2.0.x/cli/#custom-commands
@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()


# This deletes the 
@click.command(name='drop_create_tables')
@with_appcontext
def drop_create():
    db.drop_all()
    db.create_all()

# Thus custom enables the 
@click.command(name='generate_seed')
@click.argument("number")
@with_appcontext
def create_author(number):
    
    for _ in range(int(number)):
        new_user, user_login, author, book = seed_data()
        db.session.add(author)
        db.session.add(new_user)
        db.session.add(user_login)
        db.session.add(book)
    db.session.commit()
   
