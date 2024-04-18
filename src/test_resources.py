import unittest
from resource_verification import verify_asterisk_absence
from main import load_json_from_file


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
            [False, False, False]
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


if __name__ == '__main__':
    unittest.main()