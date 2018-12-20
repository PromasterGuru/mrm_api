"""Add activation field to questions relation

Revision ID: 1486dc6d0b6b
Revises: bd31f46cf430
Create Date: 2019-01-02 12:15:35.584598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1486dc6d0b6b'
down_revision = '8623c9b0aa5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('questions', 'is_active')
    # ### end Alembic commands ###