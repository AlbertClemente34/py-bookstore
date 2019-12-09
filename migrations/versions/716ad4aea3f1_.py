"""empty message

Revision ID: 716ad4aea3f1
Revises: 
Create Date: 2019-12-09 12:28:43.701751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '716ad4aea3f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('author', sa.String(), nullable=True),
    sa.Column('published', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###
