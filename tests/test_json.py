from gendiff.generate import generate_diff
import tests.expected as expected

def test_json():
    actual = generate_diff('./tests/fixtures/json_plain_before.json', 
                           './tests/fixtures/json_plain_after.json', 
                           'string')
    assert actual == expected.SIMPLE_STRING
