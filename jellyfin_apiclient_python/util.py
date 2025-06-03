import re
from datetime import datetime
from typing import Any, Optional, Dict, Type, get_type_hints, List
from uuid import UUID


def camel_to_snake(string: str) -> str:
    """Convert CAMEL_CASE to snake_case"""
    string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
    string = re.sub('([a-z0-9])([A-Z])', r'\1_\2', string)
    return string.lower()


def try_parse_child_classes(child_classes: Dict[str, Type], key: str, value: Any) -> Any:
    """Parse child classes if they need further parsing."""
    if key in child_classes:
        if isinstance(value, List):
            return [child_classes[key](item) for item in value]
        else:
            return child_classes[key](value)
    return value

def try_parse_uuid(key: str, value: Any, type_hints: Dict[str, Any]) -> Any:
    """Parse a UUID from a string."""
    if key in type_hints and type_hints[key] == Optional[UUID] and isinstance(value, str):
        try:
            return UUID(value) if value is not None else None
        except ValueError as e:
            raise ValueError(f"Failed to parse uuid: {value}, from {key}: {e}")
    return value

def try_parse_datetime(key: str, value: Any, type_hints: Dict[str, Any]) -> Any:
    """Parse a datetime from an ISO format string."""
    if key in type_hints and type_hints[key] == Optional[datetime]:
        try:
            time = datetime.fromisoformat(value.replace('Z', '+00:00'))
            return time if value is not None else None
        except ValueError as e:
            raise ValueError(f"Failed to parse datetime: {value}, from {key}: {e}")
    return value


def api_parse_single_value(instance: Any, child_classes: Optional[Dict[str, Type]], key: str, value: Any, type_hints: Dict[str, Any]) -> None:
    """
    Parse a single value from an API response.
    Args:
        instance: The object to insert the data into.
        child_classes: A dict of keys to classes if certain members need further parsing.
        key: The key to parse - must be the name of the member
        value: The value to insert
        type_hints: Type hints for the instance for parsing UUID and datetime

    Returns:
        Nothing

    Raises:
        ValueError if the UUID isn't parsed correctly.
    """
    value = try_parse_child_classes(child_classes, key, value)
    value = try_parse_uuid(key, value, type_hints)
    value = try_parse_datetime(key, value, type_hints)
    setattr(instance, key, value)

def api_parse_constructor(instance: Any, data: Optional[Dict] = None, child_classes: Optional[Dict[str, Type]] = None) -> None:
    """
    Parse a response from API to the type of instance.
    If the member is a UUID, it will be parsed to a UUID.
    Args:
        instance: The object to insert the data into.
        data: The data to insert into the instance.
        Keys are converted to snake_case to adhere to python naming standard.
        child_classes: A dict of keys to classes if certain members need further parsing.

    Returns:
        Nothing

    Raises:
        KeyError if the provided object does not contain a member of the name.
        ValueError if the UUID isn't parsed correctly.
    """
    if data is not None:
        type_hints = get_type_hints(instance)
        for key, value in data.items():
            key = camel_to_snake(key)

            if not hasattr(instance, key):
                raise KeyError(f"Key {key} is not available for {instance.__class__.__name__}")

            api_parse_single_value(instance, child_classes, key, value, type_hints)
