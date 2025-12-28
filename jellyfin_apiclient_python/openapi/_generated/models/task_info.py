from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.task_state import TaskState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_result import TaskResult
    from ..models.task_trigger_info import TaskTriggerInfo


T = TypeVar("T", bound="TaskInfo")


@_attrs_define
class TaskInfo:
    """Class TaskInfo.

    Attributes:
        name (None | str | Unset): Gets or sets the name.
        state (TaskState | Unset): Enum TaskState.
        current_progress_percentage (float | None | Unset): Gets or sets the progress.
        id (None | str | Unset): Gets or sets the id.
        last_execution_result (None | TaskResult | Unset): Gets or sets the last execution result.
        triggers (list[TaskTriggerInfo] | None | Unset): Gets or sets the triggers.
        description (None | str | Unset): Gets or sets the description.
        category (None | str | Unset): Gets or sets the category.
        is_hidden (bool | Unset): Gets or sets a value indicating whether this instance is hidden.
        key (None | str | Unset): Gets or sets the key.
    """

    name: None | str | Unset = UNSET
    state: TaskState | Unset = UNSET
    current_progress_percentage: float | None | Unset = UNSET
    id: None | str | Unset = UNSET
    last_execution_result: None | TaskResult | Unset = UNSET
    triggers: list[TaskTriggerInfo] | None | Unset = UNSET
    description: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    is_hidden: bool | Unset = UNSET
    key: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.task_result import TaskResult

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        current_progress_percentage: float | None | Unset
        if isinstance(self.current_progress_percentage, Unset):
            current_progress_percentage = UNSET
        else:
            current_progress_percentage = self.current_progress_percentage

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        last_execution_result: dict[str, Any] | None | Unset
        if isinstance(self.last_execution_result, Unset):
            last_execution_result = UNSET
        elif isinstance(self.last_execution_result, TaskResult):
            last_execution_result = self.last_execution_result.to_dict()
        else:
            last_execution_result = self.last_execution_result

        triggers: list[dict[str, Any]] | None | Unset
        if isinstance(self.triggers, Unset):
            triggers = UNSET
        elif isinstance(self.triggers, list):
            triggers = []
            for triggers_type_0_item_data in self.triggers:
                triggers_type_0_item = triggers_type_0_item_data.to_dict()
                triggers.append(triggers_type_0_item)

        else:
            triggers = self.triggers

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        is_hidden = self.is_hidden

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if state is not UNSET:
            field_dict["State"] = state
        if current_progress_percentage is not UNSET:
            field_dict["CurrentProgressPercentage"] = current_progress_percentage
        if id is not UNSET:
            field_dict["Id"] = id
        if last_execution_result is not UNSET:
            field_dict["LastExecutionResult"] = last_execution_result
        if triggers is not UNSET:
            field_dict["Triggers"] = triggers
        if description is not UNSET:
            field_dict["Description"] = description
        if category is not UNSET:
            field_dict["Category"] = category
        if is_hidden is not UNSET:
            field_dict["IsHidden"] = is_hidden
        if key is not UNSET:
            field_dict["Key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.task_result import TaskResult
        from ..models.task_trigger_info import TaskTriggerInfo

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("Name", UNSET))

        _state = d.pop("State", UNSET)
        state: TaskState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = TaskState(_state)

        def _parse_current_progress_percentage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        current_progress_percentage = _parse_current_progress_percentage(
            d.pop("CurrentProgressPercentage", UNSET)
        )

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_last_execution_result(data: object) -> None | TaskResult | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_execution_result_type_1 = TaskResult.from_dict(data)

                return last_execution_result_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskResult | Unset, data)

        last_execution_result = _parse_last_execution_result(
            d.pop("LastExecutionResult", UNSET)
        )

        def _parse_triggers(data: object) -> list[TaskTriggerInfo] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                triggers_type_0 = []
                _triggers_type_0 = data
                for triggers_type_0_item_data in _triggers_type_0:
                    triggers_type_0_item = TaskTriggerInfo.from_dict(
                        triggers_type_0_item_data
                    )

                    triggers_type_0.append(triggers_type_0_item)

                return triggers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TaskTriggerInfo] | None | Unset, data)

        triggers = _parse_triggers(d.pop("Triggers", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("Description", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("Category", UNSET))

        is_hidden = d.pop("IsHidden", UNSET)

        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("Key", UNSET))

        task_info = cls(
            name=name,
            state=state,
            current_progress_percentage=current_progress_percentage,
            id=id,
            last_execution_result=last_execution_result,
            triggers=triggers,
            description=description,
            category=category,
            is_hidden=is_hidden,
            key=key,
        )

        return task_info
