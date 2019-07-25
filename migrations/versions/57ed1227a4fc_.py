"""empty message

Revision ID: 57ed1227a4fc
Revises: 9cf0eaaf8e4e
Create Date: 2019-07-25 15:35:02.899028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57ed1227a4fc'
down_revision = '9cf0eaaf8e4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('conditions', 'length_of_stay')
    op.drop_column('conditions', 'max_lead_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('conditions', sa.Column('max_lead_time', sa.SMALLINT(), autoincrement=False, nullable=True))
    op.add_column('conditions', sa.Column('length_of_stay', sa.SMALLINT(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
