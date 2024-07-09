"""empty message

Revision ID: fcf0a1ea06bc
Revises: 8bd17d357368
Create Date: 2024-04-25 23:56:53.331871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcf0a1ea06bc'
down_revision = '8bd17d357368'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('body_html', sa.String(length=140), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.drop_column('body_html')

    # ### end Alembic commands ###