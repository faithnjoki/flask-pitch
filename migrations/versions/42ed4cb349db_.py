"""empty message

Revision ID: 42ed4cb349db
Revises: f29f791526d2
Create Date: 2020-07-20 14:26:14.042367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42ed4cb349db'
down_revision = 'f29f791526d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.drop_table('likes')
    op.drop_table('dislikes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dislikes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], name='dislikes_pitch_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='dislikes_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='dislikes_pkey'),
    sa.UniqueConstraint('user_id', name='dislikes_user_id_key')
    )
    op.create_table('likes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], name='likes_pitch_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='likes_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='likes_pkey'),
    sa.UniqueConstraint('user_id', name='likes_user_id_key')
    )
    op.drop_table('reaction')
    # ### end Alembic commands ###
