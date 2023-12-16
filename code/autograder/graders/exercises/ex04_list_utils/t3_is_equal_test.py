"""Unit tests for is_equal."""

__author__ = "730225231"

from pytest import mark


def _test_is_equal(list1: list[int], list2: list[int], expected: bool) -> None:
    """is_equal - Helper function for necessary checks"""
    from exercises.ex04_utils import is_equal
    assert is_equal(list1, list2) == expected


@mark.timeout(3)
@mark.weight(3)
def test_both_empty():
    """is_equal - Both lists are empty."""
    _test_is_equal([], [], True)


@mark.timeout(3)
@mark.weight(3)
def test_use_case1():
    """is_equal - Both lists have one matching element."""
    _test_is_equal([1], [1], True)


@mark.timeout(3)
@mark.weight(3)
def test_use_case2():
    """is_equal - Both lists are the same, with various elements."""
    _test_is_equal([1, 2, 3], [1, 2, 3], True)


@mark.timeout(3)
@mark.weight(3)
def test_diff_elements():
    """is_equal - Lists are same length, but have different elements."""
    _test_is_equal([1, 2, 3], [4, 5, 6], False)


@mark.timeout(3)
@mark.weight(3)
def test_diff_lens():
    """is_equal - Lists have the same elements, but are a different length."""
    _test_is_equal([1, 1, 1], [1, 1], False)
    _test_is_equal([1, 1], [1, 1, 1], False)


@mark.timeout(3)
@mark.weight(3)
def test_diff_len_elem():
    """is_equal - Lists have different lengths and elements."""
    _test_is_equal([1, 2], [1], False)
    _test_is_equal([1], [1, 2], False)


@mark.timeout(3)
@mark.weight(2)
def test_one_empty():
    """is_equal - Only one list is empty."""
    _test_is_equal([], [1], False)
    _test_is_equal([1], [], False)
