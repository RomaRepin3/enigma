from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base_model import BaseModel
from .rotor_block_model import RotorBlockModel
from .rotor_model import RotorModel


class RotorBlockRotorModel(BaseModel):
    """
    Модель связи блока роторов и ротора.
    """

    __tablename__ = 'rotor_block_rotor'

    rotor_id: Mapped[int] = mapped_column(ForeignKey(RotorModel.id), nullable=False, comment='Идентификатор ротора')
    rotor_block_id: Mapped[int] = mapped_column(
        ForeignKey(RotorBlockModel.id),
        nullable=False,
        comment='Идентификатор блока роторов'
    )
    rotor_position: Mapped[int] = mapped_column(Integer, nullable=False, comment='Позиция ротора в блоке')
