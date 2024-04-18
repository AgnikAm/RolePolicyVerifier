import sys
import logging
from json import JSONDecodeError
from file_input import load_json_from_file
from format_validation import validate_iam_role_policy_format, SCHEMA
from resource_verification import verify_asterisk_absence


def main():
    if len(sys.argv) != 2:
        print('Enter: python [file path to main] "[file path to json]"')
        return
    
    json_file_path = sys.argv[1]

    try:
        data = load_json_from_file(json_file_path)

    except FileNotFoundError:
        logging.error(f'File not found: {json_file_path}')
        return
    
    except JSONDecodeError as e:
        logging.error(f'Decoding error: {e}')
        return
    
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
        return
    
    if validate_iam_role_policy_format(data, SCHEMA):
        wildcard_absent = verify_asterisk_absence(data)
        print(f'Lack of wildcard "*" in Resource of subsequent statements: {wildcard_absent}')
        return wildcard_absent
    
    else:
        print('Policy document is not in AWS::IAM::Role Policy format, skipping verification of "*" in Resource.')


if __name__ == '__main__':
    main()
