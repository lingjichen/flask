"""initial migration

Revision ID: feaf6568b051
Revises: 4c32ffaed94a
Create Date: 2017-03-16 21:21:32.714774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'feaf6568b051'
down_revision = '4c32ffaed94a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('roles', 'permissions')
    # ### end Alembic commands ###
