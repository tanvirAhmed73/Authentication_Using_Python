"""upgrade password

Revision ID: 99666a757cf3
Revises: 79618da0fc60
Create Date: 2024-12-21 19:22:21.610346

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99666a757cf3'
down_revision: Union[str, None] = '79618da0fc60'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Alter the 'password' column to change its length from 50 to 200
    op.alter_column(
        'users',  # Table name
        'password',  # Column name
        type_=sa.String(200),  # New column type with 200 length
        existing_type=sa.String(50),  # Current column type with 50 length
        existing_nullable=False,  # Keep the column non-nullable
    )


def downgrade() -> None:
    # Revert the 'password' column length back from 200 to 50 if needed
    op.alter_column(
        'users',  # Table name
        'password',  # Column name
        type_=sa.String(50),  # Revert to the original column length
        existing_type=sa.String(200),  # Current column type with 200 length
        existing_nullable=False,  # Keep the column non-nullable
    )
