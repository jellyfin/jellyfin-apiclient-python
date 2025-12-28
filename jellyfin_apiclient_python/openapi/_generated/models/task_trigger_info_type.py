from enum import Enum


class TaskTriggerInfoType(str, Enum):
    DAILYTRIGGER = "DailyTrigger"
    INTERVALTRIGGER = "IntervalTrigger"
    STARTUPTRIGGER = "StartupTrigger"
    WEEKLYTRIGGER = "WeeklyTrigger"

    def __str__(self) -> str:
        return str(self.value)
