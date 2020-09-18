from typing_extensions import Final, final

cannot_change_me: Final = "cannot change me"
cannot_change_me = "trying to change me" # error: Cannot assign to final name "cannot_change_me"

print(cannot_change_me) # trying to change me

integer1: Final[int] = 42
integer1 = 66 # error: Cannot assign to final name "integer1"

class Base:
    @final
    def base_method(self) -> int:
        ...

class Derived(Base):
    def base_method(self) -> int:  # error: Cannot override final attribute "base_method" (previously declared in base class "Base")
        ...

@final
class CannotBeSubclassed:
    ...

class TryToDeriveFrom(CannotBeSubclassed):  # error: Cannot inherit from final class "CannotBeSubclassed"
    ...