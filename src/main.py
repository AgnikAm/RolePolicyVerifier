import sys
from file_input import load_json_from_file
from format_validation import validate_iam_role_policy_format, SCHEMA
from resource_verification import verify_asterisk_absence


def main():
    if len(sys.argv) != 2:
        print('Enter: python src/main.py "<json_file_path>"')
        return
    
    json_file_path = sys.argv[1]
    data = load_json_from_file(json_file_path)
    
    if validate_iam_role_policy_format(data, SCHEMA):
        wildcard_absent = verify_asterisk_absence(data)
        print(f'Lack of wildcard "*" in Resource of subsequent statements: {wildcard_absent}')
    else:
        print('Policy document is not in AWS::IAM::Role Policy format, skipping verification of "*" in Resource.')


if __name__ == '__main__':
    main()
