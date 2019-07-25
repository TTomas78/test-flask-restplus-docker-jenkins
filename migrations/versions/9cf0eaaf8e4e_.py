"""empty message

Revision ID: 9cf0eaaf8e4e
Revises: a6f7e4591bb7
Create Date: 2019-07-25 14:32:36.276886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cf0eaaf8e4e'
down_revision = 'a6f7e4591bb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client_account',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('address1', sa.String(length=100), nullable=True),
    sa.Column('address3', sa.String(length=100), nullable=True),
    sa.Column('zip_code', sa.String(length=50), nullable=True),
    sa.Column('city', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_table('conditio23ns',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('booking_counter', sa.SmallInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.drop_table('client_accounts')
    op.drop_column('conditions', 'max_occupancy')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('conditions', sa.Column('max_occupancy', sa.SMALLINT(), autoincrement=False, nullable=True))
    op.create_table('client_accounts',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('address1', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('zip_code', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('address3', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='client_accounts_pkey')
    )
    op.drop_table('conditio23ns', schema='public')
    op.drop_table('client_account', schema='public')
    # ### end Alembic commands ###