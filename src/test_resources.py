import unittest
from file_input import load_json_from_file
from resource_verification import verify_asterisk_absence


class TestResourcesVerification(unittest.TestCase):

    def test_one_statement_asterisk(self):
        self.assertEqual(
            verify_asterisk_absence(
                load_json_from_file('assets/asterisk test/one_statement_asterisk.json')
            ),
            [False]
        )


    def test_multiple_statement_asterisk(self):
        self.assertEqual(
            verify_asterisk_absence(
                load_json_from_file('assets/asterisk test/multiple_statement_asterisk.json')
            ),
            [False, False, False]
        )

    
    def test_multiple_statement_mix(self):
        self.assertEqual(
            verify_asterisk_absence(
                load_json_from_file('assets/asterisk test/multiple_statement_mix.json')
            ),
            [False, True, False]
        )

    
    def test_asterisk_nonasterisk(self):
        self.assertEqual(
            verify_asterisk_absence(
                load_json_from_file('assets/asterisk test/asterisk_nonasterisk.json')
            ),
            [False, True, False]
        )


    def test_null_resource(self):
        self.assertEqual(
            verify_asterisk_absence(
                load_json_from_file('assets/asterisk test/null_resource.json')
            ),
            [True]
        )

    
    def test_empty_list_resource(self):
        self.assertEqual(
            verify_asterisk_absence(
                load_json_from_file('assets/asterisk test/empty_list_resource.json')
            ),
            [True]
        )

    
    def test_asterisk_as_part_of_statement(self):
        self.assertEqual(
            verify_asterisk_absence(
                load_json_from_file('assets/asterisk test/asterisk_as_part_of_statement.json')
            ),
            [False, True, False]
        )


if __name__ == '__main__':
    unittest.main()