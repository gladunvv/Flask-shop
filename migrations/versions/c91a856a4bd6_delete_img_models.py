"""Delete img models

Revision ID: c91a856a4bd6
Revises: 695febf3ca1c
Create Date: 2019-06-17 00:42:01.165789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c91a856a4bd6'
down_revision = '695febf3ca1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products_picture')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products_picture',
    sa.Column('width', sa.INTEGER(), nullable=False),
    sa.Column('height', sa.INTEGER(), nullable=False),
    sa.Column('mimetype', sa.VARCHAR(length=255), nullable=False),
    sa.Column('original', sa.BOOLEAN(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('img_id', sa.INTEGER(), nullable=False),
    sa.CheckConstraint('original IN (0, 1)'),
    sa.ForeignKeyConstraint(['img_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('width', 'height', 'img_id')
    )
    # ### end Alembic commands ###
