"""empty message

Revision ID: 4e210d66af1f
Revises: fcf0a1ea06bc
Create Date: 2024-04-26 00:32:20.058618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e210d66af1f'
down_revision = 'fcf0a1ea06bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author_id', sa.Integer(), nullable=False))
        batch_op.drop_index('ix_comments_user_id')
        batch_op.create_index(batch_op.f('ix_comments_author_id'), ['author_id'], unique=False)
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['author_id'], ['id'])
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])
        batch_op.drop_index(batch_op.f('ix_comments_author_id'))
        batch_op.create_index('ix_comments_user_id', ['user_id'], unique=False)
        batch_op.drop_column('author_id')

    # ### end Alembic commands ###
