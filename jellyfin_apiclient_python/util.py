import re
from typing import Any, Optional, Dict, Type, get_type_hints, List
from uuid import UUID


def camel_to_snake(string: str) -> str:
    """Convert CAMEL_CASE to snake_case"""
    string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
    string = re.sub('([a-z0-9])([A-Z])', r'\1_\2', string)
    return string.lower()


def api_parse_constructor(instance: Any, data: Optional[Dict] = None, child_classes: Optional[Dict[str, Type]] = None):
    if data is not None:
        type_hints = get_type_hints(instance)
        for key, value in data.items():
            key = camel_to_snake(key)
            if child_classes and key in child_classes:
                if isinstance(value, List):
                    setattr(instance, key, [child_classes[key](item) for item in value])
                else:
                    setattr(instance, key, child_classes[key](value))
            elif hasattr(instance, key):
                # Check if the field is expected to be a UUID
                if key in type_hints and type_hints[key] == Optional[UUID]:
                    try:
                        setattr(instance, key, UUID(value) if value is not None else None)
                    except ValueError as e:
                        raise ValueError(f"{instance.__class__.__name__}Failed to parse uuid: {value}, from {key}: {e}")
                else:
                    setattr(instance, key, value)
            else:
                raise KeyError(f"Key {key} is not available for {instance.__class__.__name__}")
