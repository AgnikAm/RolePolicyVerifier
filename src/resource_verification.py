from typing import Any

def verify_asterisk_absence(json_data: dict[str, Any]) -> list[bool]:
    return [
        all(resource != "*" for resource in statement.get('Resource'))
        if statement.get('Resource') is not None else True
        for statement in json_data.get('PolicyDocument').get('Statement')
    ]