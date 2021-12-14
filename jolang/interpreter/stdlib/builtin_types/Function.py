from dataclasses import dataclass, field
from .object import Object
from .operator import Operator


@dataclass
class Function(Object):
    def __post_init__(self):
        Object.__init__(self)
        self._obj = self.__repr__()

    name: str
    parameters: list = field(default_factory=list)
    body: list = field(default_factory=list)
    py_bind: ... = None
    restype: ... = None
    scope: ... = None

    @Operator("Call", compatible=["Function"])
    def call(self, *args):
        pass

    def __repr__(self):
        return f"<Function {self.name!r}>"
