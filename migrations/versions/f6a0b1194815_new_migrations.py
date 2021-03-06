"""new migrations

Revision ID: f6a0b1194815
Revises: 
Create Date: 2022-02-19 13:28:35.923867

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f6a0b1194815'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('first_name', sa.String(length=200), nullable=False),
    sa.Column('last_name', sa.String(length=200), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_profile',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('first_name', sa.String(length=200), nullable=False),
    sa.Column('last_name', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=254), nullable=False),
    sa.Column('picture_url', sa.String(length=300), nullable=True),
    sa.Column('available_points', sa.Integer(), nullable=True),
    sa.Column('used_points', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('book',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=False),
    sa.Column('isbn', sa.String(length=20), nullable=True),
    sa.Column('language', sa.String(length=30), nullable=False),
    sa.Column('year_of_publication', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=300), nullable=False),
    sa.Column('author_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('owner_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('borrowed', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_available', sa.Boolean(), nullable=True),
    sa.Column('loan_points', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('cld_asset_id', sa.String(), nullable=True),
    sa.Column('cld_public_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['user_profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_login',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('password_hash', sa.String(length=200), nullable=True),
    sa.Column('google_login', sa.Boolean(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('user_profile_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_profile_id'], ['user_profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('borrow',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('borrowed_date', sa.DateTime(), nullable=True),
    sa.Column('deadline', sa.DateTime(), nullable=False),
    sa.Column('returned_date', sa.DateTime(), nullable=True),
    sa.Column('points_used', sa.Integer(), nullable=True),
    sa.Column('book_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('borrower', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['borrower'], ['user_profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('borrow')
    op.drop_table('user_login')
    op.drop_table('book')
    op.drop_table('user_profile')
    op.drop_table('author')
    # ### end Alembic commands ###
