from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base_model import BaseModel
from .rotor_block_model import RotorBlockModel
from .switching_panel_model import SwitchingPanelModel


class MachineModel(BaseModel):
    """
    Модель машины.
    """

    __tablename__ = 'machine'

    rotor_block_id: Mapped[int] = mapped_column(
        ForeignKey(RotorBlockModel.id),
        nullable=False,
        comment='Идентификатор блок роторов'
    )
    switching_panel_id: Mapped[int] = mapped_column(
        ForeignKey(SwitchingPanelModel.id),
        nullable=False,
        comment='Идентификатор коммутационной панели'
    )
