"""
Init

Revision ID: 56f74032e9c5
Revises: 
Create Date: 2024-07-14 08:46:24.517659

"""
from typing import Sequence
from typing import Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '56f74032e9c5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'reflector',
        sa.Column('a', sa.String(length=1), nullable=False, comment='Замена буквы "a"'),
        sa.Column('b', sa.String(length=1), nullable=False, comment='Замена буквы "b"'),
        sa.Column('c', sa.String(length=1), nullable=False, comment='Замена буквы "c"'),
        sa.Column('d', sa.String(length=1), nullable=False, comment='Замена буквы "d"'),
        sa.Column('e', sa.String(length=1), nullable=False, comment='Замена буквы "e"'),
        sa.Column('f', sa.String(length=1), nullable=False, comment='Замена буквы "f"'),
        sa.Column('g', sa.String(length=1), nullable=False, comment='Замена буквы "g"'),
        sa.Column('h', sa.String(length=1), nullable=False, comment='Замена буквы "h"'),
        sa.Column('i', sa.String(length=1), nullable=False, comment='Замена буквы "i"'),
        sa.Column('j', sa.String(length=1), nullable=False, comment='Замена буквы "j"'),
        sa.Column('k', sa.String(length=1), nullable=False, comment='Замена буквы "k"'),
        sa.Column('l', sa.String(length=1), nullable=False, comment='Замена буквы "l"'),
        sa.Column('m', sa.String(length=1), nullable=False, comment='Замена буквы "m"'),
        sa.Column('n', sa.String(length=1), nullable=False, comment='Замена буквы "n"'),
        sa.Column('o', sa.String(length=1), nullable=False, comment='Замена буквы "o"'),
        sa.Column('p', sa.String(length=1), nullable=False, comment='Замена буквы "p"'),
        sa.Column('q', sa.String(length=1), nullable=False, comment='Замена буквы "q"'),
        sa.Column('r', sa.String(length=1), nullable=False, comment='Замена буквы "r"'),
        sa.Column('s', sa.String(length=1), nullable=False, comment='Замена буквы "s"'),
        sa.Column('t', sa.String(length=1), nullable=False, comment='Замена буквы "t"'),
        sa.Column('u', sa.String(length=1), nullable=False, comment='Замена буквы "u"'),
        sa.Column('v', sa.String(length=1), nullable=False, comment='Замена буквы "v"'),
        sa.Column('w', sa.String(length=1), nullable=False, comment='Замена буквы "w"'),
        sa.Column('x', sa.String(length=1), nullable=False, comment='Замена буквы "x"'),
        sa.Column('y', sa.String(length=1), nullable=False, comment='Замена буквы "y"'),
        sa.Column('z', sa.String(length=1), nullable=False, comment='Замена буквы "z"'),
        sa.Column('id', sa.Integer(), nullable=False, comment='Идентификатор'),
        sa.Column('created_datetime', sa.DateTime(), nullable=False, comment='Время создания'),
        sa.Column('updated_datetime', sa.DateTime(), nullable=False, comment='Время обновления'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'rotor',
        sa.Column(
            'current_position',
            sa.Integer(),
            nullable=False,
            comment='Текущая позиция ротора, может принимать значения от 0 до 25'
        ),
        sa.Column('a', sa.String(length=1), nullable=False, comment='Замена буквы "a"'),
        sa.Column('b', sa.String(length=1), nullable=False, comment='Замена буквы "b"'),
        sa.Column('c', sa.String(length=1), nullable=False, comment='Замена буквы "c"'),
        sa.Column('d', sa.String(length=1), nullable=False, comment='Замена буквы "d"'),
        sa.Column('e', sa.String(length=1), nullable=False, comment='Замена буквы "e"'),
        sa.Column('f', sa.String(length=1), nullable=False, comment='Замена буквы "f"'),
        sa.Column('g', sa.String(length=1), nullable=False, comment='Замена буквы "g"'),
        sa.Column('h', sa.String(length=1), nullable=False, comment='Замена буквы "h"'),
        sa.Column('i', sa.String(length=1), nullable=False, comment='Замена буквы "i"'),
        sa.Column('j', sa.String(length=1), nullable=False, comment='Замена буквы "j"'),
        sa.Column('k', sa.String(length=1), nullable=False, comment='Замена буквы "k"'),
        sa.Column('l', sa.String(length=1), nullable=False, comment='Замена буквы "l"'),
        sa.Column('m', sa.String(length=1), nullable=False, comment='Замена буквы "m"'),
        sa.Column('n', sa.String(length=1), nullable=False, comment='Замена буквы "n"'),
        sa.Column('o', sa.String(length=1), nullable=False, comment='Замена буквы "o"'),
        sa.Column('p', sa.String(length=1), nullable=False, comment='Замена буквы "p"'),
        sa.Column('q', sa.String(length=1), nullable=False, comment='Замена буквы "q"'),
        sa.Column('r', sa.String(length=1), nullable=False, comment='Замена буквы "r"'),
        sa.Column('s', sa.String(length=1), nullable=False, comment='Замена буквы "s"'),
        sa.Column('t', sa.String(length=1), nullable=False, comment='Замена буквы "t"'),
        sa.Column('u', sa.String(length=1), nullable=False, comment='Замена буквы "u"'),
        sa.Column('v', sa.String(length=1), nullable=False, comment='Замена буквы "v"'),
        sa.Column('w', sa.String(length=1), nullable=False, comment='Замена буквы "w"'),
        sa.Column('x', sa.String(length=1), nullable=False, comment='Замена буквы "x"'),
        sa.Column('y', sa.String(length=1), nullable=False, comment='Замена буквы "y"'),
        sa.Column('z', sa.String(length=1), nullable=False, comment='Замена буквы "z"'),
        sa.Column('id', sa.Integer(), nullable=False, comment='Идентификатор'),
        sa.Column('created_datetime', sa.DateTime(), nullable=False, comment='Время создания'),
        sa.Column('updated_datetime', sa.DateTime(), nullable=False, comment='Время обновления'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'switching_panel',
        sa.Column('a', sa.String(length=1), nullable=False, comment='Замена буквы "a"'),
        sa.Column('b', sa.String(length=1), nullable=False, comment='Замена буквы "b"'),
        sa.Column('c', sa.String(length=1), nullable=False, comment='Замена буквы "c"'),
        sa.Column('d', sa.String(length=1), nullable=False, comment='Замена буквы "d"'),
        sa.Column('e', sa.String(length=1), nullable=False, comment='Замена буквы "e"'),
        sa.Column('f', sa.String(length=1), nullable=False, comment='Замена буквы "f"'),
        sa.Column('g', sa.String(length=1), nullable=False, comment='Замена буквы "g"'),
        sa.Column('h', sa.String(length=1), nullable=False, comment='Замена буквы "h"'),
        sa.Column('i', sa.String(length=1), nullable=False, comment='Замена буквы "i"'),
        sa.Column('j', sa.String(length=1), nullable=False, comment='Замена буквы "j"'),
        sa.Column('k', sa.String(length=1), nullable=False, comment='Замена буквы "k"'),
        sa.Column('l', sa.String(length=1), nullable=False, comment='Замена буквы "l"'),
        sa.Column('m', sa.String(length=1), nullable=False, comment='Замена буквы "m"'),
        sa.Column('n', sa.String(length=1), nullable=False, comment='Замена буквы "n"'),
        sa.Column('o', sa.String(length=1), nullable=False, comment='Замена буквы "o"'),
        sa.Column('p', sa.String(length=1), nullable=False, comment='Замена буквы "p"'),
        sa.Column('q', sa.String(length=1), nullable=False, comment='Замена буквы "q"'),
        sa.Column('r', sa.String(length=1), nullable=False, comment='Замена буквы "r"'),
        sa.Column('s', sa.String(length=1), nullable=False, comment='Замена буквы "s"'),
        sa.Column('t', sa.String(length=1), nullable=False, comment='Замена буквы "t"'),
        sa.Column('u', sa.String(length=1), nullable=False, comment='Замена буквы "u"'),
        sa.Column('v', sa.String(length=1), nullable=False, comment='Замена буквы "v"'),
        sa.Column('w', sa.String(length=1), nullable=False, comment='Замена буквы "w"'),
        sa.Column('x', sa.String(length=1), nullable=False, comment='Замена буквы "x"'),
        sa.Column('y', sa.String(length=1), nullable=False, comment='Замена буквы "y"'),
        sa.Column('z', sa.String(length=1), nullable=False, comment='Замена буквы "z"'),
        sa.Column('id', sa.Integer(), nullable=False, comment='Идентификатор'),
        sa.Column('created_datetime', sa.DateTime(), nullable=False, comment='Время создания'),
        sa.Column('updated_datetime', sa.DateTime(), nullable=False, comment='Время обновления'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'rotor_block',
        sa.Column('reflector_id', sa.Integer(), nullable=False, comment='Идентификатор рефлектора'),
        sa.Column('id', sa.Integer(), nullable=False, comment='Идентификатор'),
        sa.Column('created_datetime', sa.DateTime(), nullable=False, comment='Время создания'),
        sa.Column('updated_datetime', sa.DateTime(), nullable=False, comment='Время обновления'),
        sa.ForeignKeyConstraint(['reflector_id'], ['reflector.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'machine',
        sa.Column('rotor_block_id', sa.Integer(), nullable=False, comment='Идентификатор блок роторов'),
        sa.Column('switching_panel_id', sa.Integer(), nullable=False, comment='Идентификатор коммутационной панели'),
        sa.Column('id', sa.Integer(), nullable=False, comment='Идентификатор'),
        sa.Column('created_datetime', sa.DateTime(), nullable=False, comment='Время создания'),
        sa.Column('updated_datetime', sa.DateTime(), nullable=False, comment='Время обновления'),
        sa.ForeignKeyConstraint(['rotor_block_id'], ['rotor_block.id'], ),
        sa.ForeignKeyConstraint(['switching_panel_id'], ['switching_panel.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'rotor_block_rotor',
        sa.Column('rotor_id', sa.Integer(), nullable=False, comment='Идентификатор ротора'),
        sa.Column('rotor_block_id', sa.Integer(), nullable=False, comment='Идентификатор блока роторов'),
        sa.Column('rotor_position', sa.Integer(), nullable=False, comment='Позиция ротора в блоке'),
        sa.Column('id', sa.Integer(), nullable=False, comment='Идентификатор'),
        sa.Column('created_datetime', sa.DateTime(), nullable=False, comment='Время создания'),
        sa.Column('updated_datetime', sa.DateTime(), nullable=False, comment='Время обновления'),
        sa.ForeignKeyConstraint(['rotor_block_id'], ['rotor_block.id'], ),
        sa.ForeignKeyConstraint(['rotor_id'], ['rotor.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('rotor_block_rotor')
    op.drop_table('machine')
    op.drop_table('rotor_block')
    op.drop_table('switching_panel')
    op.drop_table('rotor')
    op.drop_table('reflector')
