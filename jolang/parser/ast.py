import inspect
import typing


class Ast:
    @staticmethod
    def format_arg(argument):
        if isinstance(argument, str):
            return repr(argument)
        return argument

    def format_args(self):
        return ", ".join(f"{x}={self.format_arg(getattr(self, x, None))}" for x in inspect.signature(self.__init__).parameters)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.format_args()})"


class Node(Ast):
    def __init__(self, argument):
        self.argument = argument


class BinaryNode(Ast):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryNode):
    pass


class Subtract(BinaryNode):
    pass


class Divide(BinaryNode):
    pass


class Multiply(BinaryNode):
    pass


class Number(Node):
    pass


class UnaryTilde(Node):
    pass


class UnaryAdd(Node):
    pass


class UnarySubtract(Node):
    pass


class UnaryLogicalNot(Node):
    pass


class String(Node):
    pass


class Constant(Node):
    pass


class Modulo(BinaryNode):
    pass


class Container(Ast):
    def __init__(self, items):
        self.items = items


class Array(Container):
    pass


class Statement(Ast):
    pass


class Body(Ast):
    def __init__(self, statements: typing.List[Statement]):
        self.statements = statements
