"""Break DB.

Revision ID: 4460566d956
Revises: 34df5956445
Create Date: 2015-05-09 15:02:46.180192

"""

# revision identifiers, used by Alembic.
revision = '4460566d956'
down_revision = '34df5956445'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admiral_ship', sa.Column('admiral_id', sa.Integer(), nullable=True))
    op.alter_column('admiral_ship', 'local_ship_num',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('admiral_ship_admiralid_fkey', 'admiral_ship', type_='foreignkey')
    op.create_foreign_key(None, 'admiral_ship', 'admiral', ['admiral_id'], ['id'])
    op.drop_column('admiral_ship', 'admiralid')
    op.add_column('dock', sa.Column('admiral_id', sa.Integer(), nullable=True))
    op.drop_constraint('dock_admiral_idea_fkey', 'dock', type_='foreignkey')
    op.create_foreign_key(None, 'dock', 'admiral', ['admiral_id'], ['id'])
    op.drop_column('dock', 'admiral_idea')
    op.add_column('ship', sa.Column('aftership_num', sa.Integer(), nullable=True))
    op.drop_column('ship', 'aftershipid')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ship', sa.Column('aftershipid', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('ship', 'aftership_num')
    op.add_column('dock', sa.Column('admiral_idea', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'dock', type_='foreignkey')
    op.create_foreign_key('dock_admiral_idea_fkey', 'dock', 'admiral', ['admiral_idea'], ['id'])
    op.drop_column('dock', 'admiral_id')
    op.add_column('admiral_ship', sa.Column('admiralid', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'admiral_ship', type_='foreignkey')
    op.create_foreign_key('admiral_ship_admiralid_fkey', 'admiral_ship', 'admiral', ['admiralid'], ['id'])
    op.alter_column('admiral_ship', 'local_ship_num',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('admiral_ship', 'admiral_id')
    ### end Alembic commands ###
