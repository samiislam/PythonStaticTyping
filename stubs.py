import random

x = chr(102)
r_int : int = random.randint(1, 22)

reveal_type(x) # note: Revealed type is 'builtins.str'
reveal_type(random.randint) # note: Revealed type is 'builtins.bool'