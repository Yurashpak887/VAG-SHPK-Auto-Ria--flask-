"""new column

Revision ID: c30de9e2f2dc
Revises: ff30d3b3ae4b
Create Date: 2023-08-27 16:56:44.389055

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c30de9e2f2dc'
down_revision = 'ff30d3b3ae4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('country_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
        batch_op.create_foreign_key(None, 'country', ['country_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('country_id',
               existing_type=mysql.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
