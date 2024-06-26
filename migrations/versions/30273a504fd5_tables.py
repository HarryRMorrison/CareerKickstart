"""tables

Revision ID: 30273a504fd5
Revises: 2a7acf4c71bc
Create Date: 2024-05-18 17:06:15.420481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30273a504fd5'
down_revision = '2a7acf4c71bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('tag_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tag', sa.String(length=40), nullable=True),
    sa.Column('category', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('tag_id'),
    sa.UniqueConstraint('tag')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=30), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('profile_pic', sa.String(length=12), nullable=True),
    sa.Column('about_me', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('questions',
    sa.Column('question_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=2000), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('comments', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('question_id')
    )
    op.create_table('answers',
    sa.Column('ans_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('answer', sa.String(length=2000), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['questions.question_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('ans_id')
    )
    op.create_table('question_tags',
    sa.Column('qt_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['questions.question_id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.tag_id'], ),
    sa.PrimaryKeyConstraint('qt_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question_tags')
    op.drop_table('answers')
    op.drop_table('questions')
    op.drop_table('users')
    op.drop_table('tags')
    # ### end Alembic commands ###
