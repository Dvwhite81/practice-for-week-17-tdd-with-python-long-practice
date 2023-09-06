from app.roman_numerals import parse
from pytest import mark

test_numerals = [
    ("XI", 11),
    ("XIV", 14),
    ("XIX", 19),
    ("XX", 20),
    ("XXXIV", 34),
    ("XLI", 41),
    ("L", 50),
    ("XCIX", 99),
    ("C", 100),
    ("CCCXXXIII", 333),
    ("DLV", 555),
    ("CDXLIX", 449),
    ("MCMLXXII", 1972)
]

# @mark.parametrize("input, expected", [("IX", 9), ("X", 10)])
# def test_roman_numeral_parser(input, expected):
#    value = parse(input)

#    assert value == expected

@mark.parametrize("input, expected", test_numerals)
def test_roman_numeral_parser(input, expected):
    value = parse(input)

    assert value == expected
