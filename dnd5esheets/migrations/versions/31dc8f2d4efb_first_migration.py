"""First migration

Revision ID: 31dc8f2d4efb
Revises:
Create Date: 2023-06-22 10:09:46.696271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "31dc8f2d4efb"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "party",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "player",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "character",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("slug", sa.String(length=255), nullable=False),
        sa.Column("class", sa.String(length=80), nullable=False),
        sa.Column("level", sa.Integer(), nullable=False),
        sa.Column("json_data", sa.Text(), nullable=False),
        sa.Column("player_id", sa.Integer(), nullable=False),
        sa.Column("party_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["party_id"],
            ["party.id"],
        ),
        sa.ForeignKeyConstraint(
            ["player_id"],
            ["player.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("character")
    op.drop_table("player")
    op.drop_table("party")
    # ### end Alembic commands ###
