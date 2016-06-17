def uppercases_all_letters(str):
  STR = str.upper()
  return STR

# -----------------------------------------------------------------------------

# These are the automated tests for this exercise. Do not modify them at all.
# When you run `bin/check`, these tests will report on the validity of your
# algorithm.

def test_hello():
  assert uppercases_all_letters("hello") == "HELLO"

def test_HELLO():
  assert uppercases_all_letters("HELLO") == "HELLO"

def test_scooby_doo():
  assert uppercases_all_letters("scooby doo") == "SCOOBY DOO"