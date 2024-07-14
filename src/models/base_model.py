from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base


class BaseModel(Base):
    """
    Метаданные моделей БД.
    """

    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, comment='Идентификатор')
    created_datetime: Mapped[datetime] = mapped_column(nullable=False, default=func.now(), comment='Время создания')
    updated_datetime: Mapped[datetime] = mapped_column(
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
        comment='Время обновления'
    )
