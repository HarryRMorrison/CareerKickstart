"""index for tags

Revision ID: 8ca5e375ee80
Revises: e38033ffec10
Create Date: 2024-05-13 12:46:15.004530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ca5e375ee80'
down_revision = 'e38033ffec10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_tags_category'), ['category'], unique=False)
        batch_op.create_index(batch_op.f('ix_tags_tag'), ['tag'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_tags_tag'))
        batch_op.drop_index(batch_op.f('ix_tags_category'))

    # ### end Alembic commands ###