"""Add local_fleet_id to AdmiralShip

Revision ID: 400372d482a
Revises: d0b75f5d47
Create Date: 2015-05-08 19:18:40.835525

"""

# revision identifiers, used by Alembic.
revision = '400372d482a'
down_revision = 'd0b75f5d47'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admiral_ship', sa.Column('local_fleet_id', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('admiral_ship', 'local_fleet_id')
    ### end Alembic commands ###
