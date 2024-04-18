from typing import Any


def verify_asterisk_absence(json_data: dict[str, Any]) -> list[bool]:
    """
    Verify the absence of asterisks (*) in the "Resource" field of IAM policy statements.

    Args:
        json_data (dict): A dictionary representing the IAM role policy data.

    Returns:
        list[bool]: A list of boolean values indicating whether each IAM policy statement
        in the provided JSON data contains an asterisk (*) in the "Resource" field.
        True indicates absence of asterisk, False indicates presence of asterisk.
    """
    return [
        all(resource != "*" for resource in statement.get('Resource'))
        if statement.get('Resource') is not None else True
        for statement in json_data.get('PolicyDocument').get('Statement')
    ]