import re
from jsonschema import validate
from file_input import load_json_from_file
from typing import Any

POLICY_NAME_PATTERN = r'[\w+=,.@-]+'
POLICY_NAME_MIN_LENGTH = 1
POLICY_NAME_MAX_LENGTH = 128
SCHEMA = load_json_from_file('assets/schema/aws-iam-poilcy-schema.json')


def validate_iam_role_policy_format(json_data: dict[str, Any], schema: dict[str, Any]) -> bool:
    """
    Validate the format of an IAM role policy.

    Args:
        json_data (dict): The JSON data representing the IAM role policy.
        schema (dict): The JSON schema for IAM role policies.

    Returns:
        bool: True if the policy format is valid, False otherwise.
    """
    return is_valid_policy_name(json_data) and is_valid_policy_document(json_data, schema)


def is_valid_policy_name(json_data: dict[str, Any]) -> bool:
    """Check if the policy name in the IAM role policy data is valid."""
    if 'PolicyName' not in json_data:
        return False
    
    policy_name = json_data['PolicyName']

    return\
        isinstance(policy_name, str) and\
        is_of_length(policy_name) and\
        is_of_pattern(policy_name)
            

def is_of_length(name: str) -> bool:
    """Check if length of the name is within the allowed range."""
    return POLICY_NAME_MIN_LENGTH <= len(name) <= POLICY_NAME_MAX_LENGTH


def is_of_pattern(name: str) -> bool:
    """Check if the name matches the specified pattern."""
    return re.fullmatch(POLICY_NAME_PATTERN, name) is not None


def is_valid_policy_document(json_data: dict[str, Any], schema: dict[str, Any]) -> bool:
    """Validate the IAM role policy document against the provided schema."""
    if 'PolicyDocument' not in json_data:
        return False
        
    try:
        validate(instance=json_data['PolicyDocument'], schema=schema)
        return True
    
    except:
        return False
    