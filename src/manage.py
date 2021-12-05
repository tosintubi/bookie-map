import click
from flask.cli import with_appcontext

from src import db
# from src.models import  Author, Book, Borrow, UserLogin, UserProfile

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()
