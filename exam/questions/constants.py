"""Define constants with dataclasses for use in an executable examination."""

from dataclasses import dataclass


# exception constant
@dataclass(frozen=True)
class ExceptionLabel:
    """Define the Exception dataclass for constant(s)."""

    Exception: str


exception = ExceptionLabel(Exception="Exception")


# fuzzing constant
@dataclass(frozen=True)
class Fuzzing:
    """Define the Fuzzing dataclass for constant(s)."""

    Empty_String: str


# create an instance of the Fuzzing dataclass
fuzzing = Fuzzing(Empty_String="")


# triangle constant
@dataclass(frozen=True)
class Triangle:
    """Define the Triangle dataclass for constant(s)."""

    Equilateral: str
    Isosceles: str
    Scalene: str


# create an instance of the Triangle dataclass
triangle = Triangle(Equilateral="Equilateral", Isosceles="Isosceles", Scalene="Scalene")


# recursion constant
@dataclass(frozen=True)
class Recursion:
    """Define the Recursion dataclass for constant(s)."""

    basecase: int
    basecase_return: int


# create an instance of the Recursion dataclass
recursion = Recursion(basecase=1, basecase_return=1)
