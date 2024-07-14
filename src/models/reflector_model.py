from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base_model import BaseModel


class ReflectorModel(BaseModel):
    """
    Модель рефлектора.
    """

    __tablename__ = 'reflector'

    a: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "a"')
    b: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "b"')
    c: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "c"')
    d: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "d"')
    e: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "e"')
    f: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "f"')
    g: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "g"')
    h: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "h"')
    i: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "i"')
    j: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "j"')
    k: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "k"')
    l: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "l"')
    m: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "m"')
    n: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "n"')
    o: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "o"')
    p: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "p"')
    q: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "q"')
    r: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "r"')
    s: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "s"')
    t: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "t"')
    u: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "u"')
    v: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "v"')
    w: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "w"')
    x: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "x"')
    y: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "y"')
    z: Mapped[str] = mapped_column(String(1), nullable=False, comment='Замена буквы "z"')
