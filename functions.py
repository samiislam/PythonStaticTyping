from typing import List, Iterable

def echo(message):
  return 'Echo ' + message

def echo2(message : str) -> str:
    return 'Echo2 ' + message

def func_does_not_return() -> None:
  print("I don't return")

r = func_does_not_return() # error: "func_does_not_return" does not return a value

def func_arg_with_default_values(arg1 : int, arg2 : bool = True) -> None:
    ...

def func_star_args(*args: int, **kwargs: str) -> None:
    ...

def numbers_with_squares_less100(numbers: Iterable[int]) -> List[int]:
    returnList = []
    
    for num in numbers:
      if num*num < 100:
        returnList.append(num)
    return returnList

def f(l: List[object]) -> None:
    l = [1, 2]
    reveal_type(l)

def use_list_of_integers(ints: List[int]) -> None:
    print('Items:', ''.join(str(i) for i in ints))

use_list_of_integers([])