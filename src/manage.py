import click
from flask.cli import with_appcontext

from src import db


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
