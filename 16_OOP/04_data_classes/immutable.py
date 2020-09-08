from dataclasses import dataclass


# frozen parameter makes the class immutable
# useful when you want the class to represent data that isn't going to change
@dataclass(frozen=True)     # immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def someFunc(self, newval):
        self.value2 = newval


obj = ImmutableClass()
print(obj.value1)

# # attempt to change immutable
# obj.value1 = "another value"
# print(obj.value1)       # frozen instance error = immutable
# obj.someFunc(20)        # frozen instance error = immutable
