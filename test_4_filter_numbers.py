def filter_numbers(arr):
  arr_f = []
  for item in arr:
    if item < 10:
      arr_f.append(item)
  return arr_f

# -----------------------------------------------------------------------------

# These are the automated tests for this exercise. Do not modify them at all.
# When you run `bin/check`, these tests will report on the validity of your
# algorithm.

def test_removes_92():
  assert filter_numbers([3, 92]) == [3]

def test_removes_10_and_greater():
  assert filter_numbers([30, 5, 9, 10, 11]) == [5, 9]

def test_removes_big_numbers_including_decimals():
  assert filter_numbers([50, 49.5, 30.00, 5, 6, 0, 10]) == [5, 6, 0]

def test_removes_no_numbers():
  assert filter_numbers([3, 6, 7, 0, 2]) == [3, 6, 7, 0, 2]