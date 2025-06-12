import uuid

def verify_uuid(uuid_str: str):
    try:
        uuid.UUID(uuid_str)
    except ValueError as e:
        raise RuntimeError(f"Invalid uuid {uuid_str}: {e}") from e