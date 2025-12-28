from enum import Enum


class DynamicDayOfWeek(str, Enum):
    EVERYDAY = "Everyday"
    FRIDAY = "Friday"
    MONDAY = "Monday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
    THURSDAY = "Thursday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    WEEKDAY = "Weekday"
    WEEKEND = "Weekend"

    def __str__(self) -> str:
        return str(self.value)
