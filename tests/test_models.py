"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest



# will replace these two functions with one parametrized one

# def test_daily_mean_zeros():
#     """Test that mean function works for an array of zeros."""
#     from inflammation.models import daily_mean
#
#     test_input = np.array([[0, 0],
#                            [0, 0],
#                            [0, 0]])
#     test_result = np.array([0, 0])
#
#     # Need to use Numpy testing functions to compare arrays
#     npt.assert_array_equal(daily_mean(test_input), test_result)
#
#

# def test_daily_mean_integers():
#     """Test that mean function works for an array of positive integers."""
#     from inflammation.models import daily_mean
#
#     test_input = np.array([[1, 2],
#                            [3, 4],
#                            [5, 6]])
#     test_result = np.array([3, 4])
#
#     # Need to use Numpy testing functions to compare arrays
#     npt.assert_array_equal(daily_mean(test_input), test_result)
#


@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
    ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.models import daily_mean
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))


# def test_daily_max_zeros():
#     """Test that max function works for an array of positive integers."""
#     from inflammation.models import daily_max
#
#     test_input = np.array([[4, 2, 5],
#                            [1, 6, 2],
#                            [4, 1, 9]])
#     test_result = np.array([4, 6, 9])
#
#     npt.assert_array_equal(daily_max(test_input), test_result)
#
#
# def test_daily_min():
#     """Test that min function works for an array of positive and negative integers."""
#     from inflammation.models import daily_min
#
#     test_input = np.array([[ 4, -2, 5],
#                            [ 1, -6, 2],
#                            [-4, -1, 9]])
#     test_result = np.array([-4, -6, 2])
#
#     npt.assert_array_equal(daily_min(test_input), test_result)


@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0, 0], [0, 0, 0], [0, 0, 0] ], [0, 0, 0]),
        ([ [4, 2, 5], [1, 6, 2], [4, 1, 9] ], [4, 6, 9]),
        ([ [4, -2, 5], [1, -6, 2], [-4, -1, 9] ], [4, -1, 9]),
    ])
def test_daily_max(test, expected):
    """Test max function works for zeroes, positive integers, mix of positive/negative integers."""
    from inflammation.models import daily_max
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))



@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0, 0], [0, 0, 0], [0, 0, 0] ], [0, 0, 0]),
        ([ [4, 2, 5], [1, 6, 2], [4, 1, 9] ], [1, 1, 2]),
        ([ [4, -2, 5], [1, -6, 2], [-4, -1, 9] ], [-4, -6, 2]),
    ])
def test_daily_min(test, expected):
    """Test min function works for zeroes, positive integers, mix of positive/negative integers."""
    from inflammation.models import daily_min
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))


def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])

# Code review Test STD code: daily_std() function
#     test_input = np.array([[0, 0],
#                            [0, 0],
#                            [0, 0]])
#     test_result = np.array([0, 0])
@pytest.mark.parametrize(
    "test, expected",
    [
        ([1, 2, 3, 4, 5], [1.4142135623730951]),
        ([23, 4, 6, 457, 65, 7, 45, 8], 145.13565852332775)
    ])
def test_daily_std():
    """Test  daily_std() function."""
    npt.assert_array_equal(daily_std(np.array(test)), np.array(expected))