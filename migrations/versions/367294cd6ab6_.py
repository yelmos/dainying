"""empty message

Revision ID: 367294cd6ab6
Revises: d6fad34d308f
Create Date: 2018-11-22 18:18:43.845920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '367294cd6ab6'
down_revision = 'd6fad34d308f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=True),
    sa.Column('email', sa.String(length=20), nullable=True),
    sa.Column('token', sa.String(length=256), nullable=True),
    sa.Column('icon', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
