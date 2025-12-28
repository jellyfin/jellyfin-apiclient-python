from enum import Enum


class ProfileConditionType(str, Enum):
    EQUALS = "Equals"
    EQUALSANY = "EqualsAny"
    GREATERTHANEQUAL = "GreaterThanEqual"
    LESSTHANEQUAL = "LessThanEqual"
    NOTEQUALS = "NotEquals"

    def __str__(self) -> str:
        return str(self.value)
