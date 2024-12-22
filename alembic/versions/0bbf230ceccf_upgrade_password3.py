"""upgrade password3

Revision ID: 0bbf230ceccf
Revises: 99666a757cf3
Create Date: 2024-12-21 19:43:11.069415

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0bbf230ceccf'
down_revision: Union[str, None] = '99666a757cf3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Ensure the table exists and modify the password column to increase its length
    op.alter_column('users', 'password', type_=sa.String(200), existing_type=sa.String(50))

def downgrade() -> None:
    # Revert the password column back to its original length of 50
    op.alter_column('users', 'password', type_=sa.String(50), existing_type=sa.String(200))

