import unittest
from format_validation import validate_iam_role_policy_format
from main import load_json_from_file, SCHEMA


class TestFormatValidation(unittest.TestCase):
    valid_files_paths = [
        "assets/format test/one_statement.json",
        "assets/format test/multiple_statements.json",
    ]

    invalid_files_paths = [
        'assets/format test/no_policy_name.json',
        'assets/format test/wrong_length_policy_name.json',
        'assets/format test/forbidden_char_policy_name.json',
        'assets/format test/no_policy_document.json',
        'assets/format test/no_version_policy_document.json',
        'assets/format test/no_sid.json',
        'assets/format test/no_effect.json',
        'assets/format test/no_action.json',
        'assets/format test/no_resource.json',
        'assets/format test/wrong_resource.json'
    ]

    valid_files = [load_json_from_file(path) for path in valid_files_paths]
    invalid_files = [load_json_from_file(path) for path in invalid_files_paths]


    def test_valid_policy_document(self):
        for test_data in self.valid_files:
            with self.subTest(data=test_data):
                self.assertTrue(validate_iam_role_policy_format(test_data, SCHEMA))
        

    def test_invalid_policy_document(self):
        for test_data in self.invalid_files:
            with self.subTest(data=test_data):
                self.assertFalse(validate_iam_role_policy_format(test_data, SCHEMA))


if __name__ == '__main__':
    unittest.main()