from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base_model import BaseModel
from .reflector_model import ReflectorModel


class RotorBlockModel(BaseModel):
    """
    Модель блока роторов.
    """

    __tablename__ = 'rotor_block'

    reflector_id: Mapped[int] = mapped_column(
        ForeignKey(ReflectorModel.id),
        nullable=False,
        comment='Идентификатор рефлектора'
    )
