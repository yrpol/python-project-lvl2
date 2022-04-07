from gendiff.generate import generate_diff
import tests.expected as expected

def test_json_plain():
    actual = generate_diff('../fixtures/jsin_plain_before.json', 
                         '../fixtures/jsin_plain_after.json', 
                         'string')
    assert actual == expected.SIMPLE_STRING