"""Initial migration

Revision ID: 79618da0fc60
Revises: 
Create Date: 2024-12-21 19:19:03.143806

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '79618da0fc60'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the users table
    op.create_table(
        'users',
        sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('username', mysql.VARCHAR(length=20), nullable=False),
        sa.Column('email', mysql.VARCHAR(length=50), nullable=False),
        sa.Column('password', mysql.VARCHAR(length=50), nullable=False),
        sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint('id'),
        mysql_collate='utf8mb4_0900_ai_ci',
        mysql_default_charset='utf8mb4',
        mysql_engine='InnoDB'
    )
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.create_index('ix_users_email', 'users', ['email'], unique=False)


def downgrade() -> None:
    # Drop the users table if downgrading
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('ix_users_id', table_name='users')
    op.drop_table('users')
