"""Upgrade password field length

Revision ID: 6ef95854aeea
Revises: 0bbf230ceccf
Create Date: 2024-12-21 19:46:01.633581

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '6ef95854aeea'
down_revision: Union[str, None] = '0bbf230ceccf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Alter the password column to change its length from 50 to 200
    op.alter_column('users', 'password', type_=sa.String(200), existing_type=sa.String(50))


def downgrade() -> None:
    # Revert the password column to its original length of 50
    op.alter_column('users', 'password', type_=sa.String(50), existing_type=sa.String(200))
