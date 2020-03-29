"""question table

Revision ID: 92447109d19c
Revises: 370bc638a080
Create Date: 2020-03-29 23:06:08.367055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92447109d19c'
down_revision = '370bc638a080'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('modul', sa.String(length=100), nullable=False),
    sa.Column('question', sa.String(length=250), nullable=False),
    sa.Column('solution', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('question')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question')
    # ### end Alembic commands ###
