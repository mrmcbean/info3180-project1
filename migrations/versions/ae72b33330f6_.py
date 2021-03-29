"""empty message

Revision ID: ae72b33330f6
Revises: 3acea2489108
Create Date: 2021-03-28 16:01:36.734610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae72b33330f6'
down_revision = '3acea2489108'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=800), nullable=True),
    sa.Column('numberOfRooms', sa.String(length=20), nullable=True),
    sa.Column('numberOfBathrooms', sa.String(length=20), nullable=True),
    sa.Column('price', sa.String(length=80), nullable=True),
    sa.Column('location', sa.String(length=200), nullable=True),
    sa.Column('propertyType', sa.String(length=80), nullable=True),
    sa.Column('photo', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('property')
    # ### end Alembic commands ###