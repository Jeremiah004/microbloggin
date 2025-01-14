"""empty message

Revision ID: 8bd17d357368
Revises: 12942726b4a9
Create Date: 2024-04-25 00:22:01.043379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bd17d357368'
down_revision = '12942726b4a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('language', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_comments_post_id'), ['post_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_comments_timestamp'), ['timestamp'], unique=False)
        batch_op.create_index(batch_op.f('ix_comments_user_id'), ['user_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_comments_user_id'))
        batch_op.drop_index(batch_op.f('ix_comments_timestamp'))
        batch_op.drop_index(batch_op.f('ix_comments_post_id'))

    op.drop_table('comments')
    # ### end Alembic commands ###
