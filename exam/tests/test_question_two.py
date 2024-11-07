"""Confirm the correctness of functions in question_two."""

import pytest

# ruff: noqa: PLR2004
from questions.question_two import (
    check_print_violations_in_functions,
    count_minus_operator_in_assignments,
    count_plus_operator_in_assignments,
    count_print_functions_linter,
    detect_print_function_violation_linter,
    has_overall_print_violation_linter,
)

source_code_one_three_prints = """
def example_function():
    print("Hello, World!")
    print("This is a test.")
    x = 10
    if x > 5:
        print("x is greater than 5")
"""

source_code_one_three_prints_embedded_print = """
def example_function():
    print("Hello, World!")
    print("This is a test.")
    x = 10
    if x > 5:
        print("print x is greater than 5")
"""

source_code_one_zero_prints = """
def example_function():
    x = 10
    if x > 5:
        x = 5
"""

source_code_one_zero_prints_embedded_print = """
def example_function():
    x = 10
    if x > 5:
        x = 5
        example = "print x is greater than 5"
"""

source_code_two_one_plus = """
def example_function():
    print("Hello, World!")
    print("This is a test.")
    x = x + 10
    if x > 5:
        print("x + 10 is greater than 5")
"""

source_code_two_one_minus = """
def example_function():
    print("Hello, World!")
    print("This is a test.")
    x = x - 10
    if x > 5:
        print("x - 10 is greater than 5")
"""


@pytest.mark.question_two_part_a
def test_extract_prints_from_source_code():
    """Test for a question part."""
    count = count_print_functions_linter(source_code_one_three_prints)
    assert (
        count == 3
    ), "Failed to count the number of print functions in the source code"


@pytest.mark.question_two_part_a
def test_extract_prints_from_source_code_embedded_print():
    """Test for a question part."""
    count = count_print_functions_linter(source_code_one_three_prints_embedded_print)
    assert (
        count == 3
    ), "Failed to count the number of print functions in the source code with a print string"


@pytest.mark.question_two_part_a
def test_zero_prints_in_source_code():
    """Test for a question part."""
    count = count_print_functions_linter(source_code_one_zero_prints)
    assert (
        count == 0
    ), "Failed to count the number of print functions in the source code with zero print statements"


@pytest.mark.question_two_part_a
def test_zero_prints_in_source_code_embedded():
    """Test for a question part."""
    count = count_print_functions_linter(source_code_one_zero_prints_embedded_print)
    assert (
        count == 0
    ), "Failed to count the number of print functions in the source code with zero print statements and embedded strings"


@pytest.mark.question_two_part_a
def test_extract_prints_from_source_code_check_violation():
    """Test for a question part."""
    count = count_print_functions_linter(source_code_one_three_prints)
    assert (
        count == 3
    ), "Failed to count the number of print functions in the source code"
    not_violation = detect_print_function_violation_linter(
        source_code_one_three_prints, 2
    )
    assert not_violation, "Failed to detect the violation of the print function limit"
    expected_violation = detect_print_function_violation_linter(
        source_code_one_three_prints
    )
    assert (
        expected_violation
    ), "Failed to detect the violation of the default print function limit"


@pytest.mark.question_two_part_b
def test_extract_plus_operator_from_source_code():
    """Test for a question part."""
    count = count_plus_operator_in_assignments(source_code_two_one_plus)
    assert (
        count == 1
    ), "Failed to count the number of plus operators in the source code (exist)"
    count = count_plus_operator_in_assignments(source_code_two_one_minus)
    assert (
        count == 0
    ), "Failed to count the number of plus operators in the source code (not exist)"


@pytest.mark.question_two_part_b
def test_extract_minus_operator_from_source_code():
    """Test for a question part."""
    count = count_minus_operator_in_assignments(source_code_two_one_minus)
    assert (
        count == 1
    ), "Failed to count the number of minus operators in the source code (exist)"
    count = count_minus_operator_in_assignments(source_code_two_one_plus)
    assert (
        count == 0
    ), "Failed to count the number of minus operators in the source code (not exist)"


@pytest.mark.question_two_part_c
def test_check_print_violations_with_list():
    """Test for a question part."""
    # create a list of source codes
    source_codes = [
        source_code_one_three_prints,
        source_code_one_three_prints_embedded_print,
        source_code_one_zero_prints,
        source_code_one_zero_prints_embedded_print,
    ]
    # check the violations of print functions in the list
    violations = check_print_violations_in_functions(source_codes)
    # expected results
    expected_violations = {
        source_code_one_three_prints: True,
        source_code_one_three_prints_embedded_print: True,
        source_code_one_zero_prints: False,
        source_code_one_zero_prints_embedded_print: False,
    }
    # assert the results
    assert (
        violations == expected_violations
    ), "Failed to check the violations of print functions in the list"


@pytest.mark.question_two_part_d
def test_check_overall_violations():
    """Test for a question part."""
    # create a list of source codes
    source_codes = [
        source_code_one_three_prints,
        source_code_one_three_prints_embedded_print,
        source_code_one_zero_prints,
        source_code_one_zero_prints_embedded_print,
    ]
    # check the violations of print functions in the list
    violations = check_print_violations_in_functions(source_codes)
    # expected results
    expected_violations = {
        source_code_one_three_prints: True,
        source_code_one_three_prints_embedded_print: True,
        source_code_one_zero_prints: False,
        source_code_one_zero_prints_embedded_print: False,
    }
    # assert the results
    assert violations == expected_violations
    # check the violations of plus operators in the list
    violations = check_print_violations_in_functions(source_codes)
    # expected results
    overall_violations = has_overall_print_violation_linter(violations)
    # assert the results
    assert (
        overall_violations
    ), "Failed to check the overall violations of print functions in the list"
