from app import bubble_sort
import pytest

#testy do funkcji bubble_sort z app.py napisane na 3 sposoby:

def test_bubble_sort1():
    got = bubble_sort([4, 8, 5, 9, 3, 1])
    want = [1, 3, 4, 5, 8, 9]

    assert got == want


testdata1 = [[4, 8, 6, 1, 12, 9]]

@pytest.mark.parametrize('unsorted_list', testdata1)
def test_bubble_sort2(unsorted_list):

    sorted = bubble_sort(unsorted_list)

    assert sorted == [1, 4, 6, 8, 9, 12]


testdata2 = [([4, 2, 6, 7, 8, 3, 9, 1], [1, 2, 3, 4, 6, 7, 8, 9])]

@pytest.mark.parametrize('unsorted_list, expected_output', testdata2)
def test_bubble_sort3(unsorted_list, expected_output):
    assert bubble_sort(unsorted_list) == expected_output