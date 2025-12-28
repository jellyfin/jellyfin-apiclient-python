from enum import Enum


class TaskTriggerInfoDayOfWeek(str, Enum):
    FRIDAY = "Friday"
    MONDAY = "Monday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
    THURSDAY = "Thursday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"

    def __str__(self) -> str:
        return str(self.value)
