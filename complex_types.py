from typing import Any, List, Tuple, Callable, Union, Optional, NoReturn, NewType, TypedDict, ClassVar, Dict, Set

class ClassA:
    def MethodA(self) -> int:  # Type of self inferred (A)
        return 42

def UseClassA(a: ClassA) -> None:
    print(a.MethodA())
    a.MethodB()

a : ClassA = ClassA()
UseClassA(a)

class ClassB:
    i: int  # Instance variable
    s: ClassVar[str]  # Class variable

    def method(self) -> None:
        self.i = 0  # OK
        self.s = 'test'  # error: Cannot assign to class variable "s" via instance

ClassB.s = 'assign'  # This is OK

a1 : Any = "ANY"
i1 : int = 42
a1 = {4, 54}
reveal_type(a1) # note: Revealed type is 'Any'
print(a1) # {4, 54}
i1 = a1
reveal_type(i1) # note: Revealed type is 'builtins.int'
print(i1) # {4, 54}

def f(tup: Tuple[int, str]) -> None:
    tup = 42, 'forty-two'
    tup = 'forty-two', 42 # error: Incompatible types in assignment (expression has type "Tuple[str, int]", variable has type "Tuple[int, str]")

def tuples(t: Tuple[int, ...]) -> None:
    for item in t:
        print(item)

def use_callable(i: int, c: Callable[[int], str]) -> str:
    return c(i)

def drawstars(i: int) -> str:
    return '*'*i

print(use_callable(5, drawstars)) # *****


def use_union(u: Union[int, str]) -> None:
    u + 42     # Error: since the type of u can be str
    if isinstance(u, str):
        print(u + 'Mypy')
    else:
        print(u + 8)

use_union('Hello ')
use_union(5)

def use_optional(o: Optional[int]) -> int:
    o_new = o + 44 # error: Unsupported operand types for + ("None" and "int")
    if o is None:
        return 42
    else:
        return o + 1

def use_noreturn() -> NoReturn:
    raise Exception('no return value')
    return 'BlahBlahBlah' # not an error

PartId = NewType('PartId', int)

handle : PartId = 67 # error: Incompatible types in assignment (expression has type "int", variable has type "PartId")
wheel : PartId = PartId(67)
reveal_type(wheel) # note: Revealed type is 'complex_types.PartId'

PersonalInformation = TypedDict('PersonalInformation', {'name': str, 'age': int})

customer : PersonalInformation = {'name': 'John Smith', 'age': 39}

print(f"Name={customer['name']}, Age={customer['age']}")

c1 : Union[Dict[Tuple[float, str], Set[int]], List[int]]
simpleRep = Union[Dict[Tuple[float, str], Set[int]], List[int]]
c2 : simpleRep

def FuncF(x: ClassC) -> None: # Exception has occurred: NameError name 'ClassC' is not defined
    ...

class ClassC:
    ...