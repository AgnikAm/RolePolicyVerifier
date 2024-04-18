import re
from jsonschema import validate
from file_input import load_json_from_file
from typing import Any

POLICY_NAME_PATTERN = r'[\w+=,.@-]+'
POLICY_NAME_MIN_LENGTH = 1
POLICY_NAME_MAX_LENGTH = 128
SCHEMA = load_json_from_file('assets/schema/aws-iam-poilcy-schema.json')


def validate_iam_role_policy_format(json_data: dict[str, Any], schema: dict[str, Any]) -> bool:
    return is_valid_policy_name(json_data) and is_valid_policy_document(json_data, schema)


def is_valid_policy_name(json_data: dict[str, Any]) -> bool:
    if 'PolicyName' not in json_data:
        return False
    
    policy_name = json_data['PolicyName']

    return\
        isinstance(policy_name, str) and\
        is_of_length(policy_name) and\
        is_of_pattern(policy_name)
            

def is_of_length(key: str) -> bool:
    return POLICY_NAME_MIN_LENGTH <= len(key) <= POLICY_NAME_MAX_LENGTH


def is_of_pattern(key: str) -> bool:
    return re.fullmatch(POLICY_NAME_PATTERN, key) is not None


def is_valid_policy_document(json_data: dict[str, Any], schema: dict[str, Any]) -> bool:
    if 'PolicyDocument' not in json_data:
        return False
        
    validate(instance=json_data['PolicyDocument'], schema=schema)
    return True
    