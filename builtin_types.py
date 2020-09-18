from typing import List, Set, Dict, Tuple, Union

i = 5
j : int = 8

i = "five" # error: Incompatible types in assignment (expression has type "str", variable has type "int")
j = [3, 4, 5] # error: Incompatible types in assignment (expression has type "List[int]", variable has type "int")

s1 , b1 = "mypy1", True # type: str, bool

s1 = 6 # error: Incompatible types in assignment (expression has type "int", variable has type "str")
b1 = { 
        "test1" : "one", 
        "test2" : "two" 
     } # error: Incompatible types in assignment (expression has type "Dict[str, str]", variable has type "bool")

l : List[Union[str, int, List[str]]] = [ "one", 2, [ "three" ] ]

l = ( 
        4, 
        "two", 
        [ 6 ] 
    ) # error: Incompatible types in assignment (expression has type "Tuple[int, str, List[int]]", variable has type "List[object]")

t = (5, 3, 6)
t = { 
        1 : "one", 
        2 : "two" 
    } # error: Incompatible types in assignment (expression has type "Dict[int, str]", variable has type "Tuple[int, int, int]")

ii: int = 1
f: float = 1.0
b: bool = True
s: str = "test"
aob: bytes = b"test"
ll: List[int] = [3, 4, 1]
se: Set[int] = {44, 86}
d: Dict[int, str] = { 7 : 'seven' }
tt: Tuple[str, int, float] = ("one", 2, 3.5)
reveal_type({44, 86})