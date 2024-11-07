"""Confirm the correctness of functions in question_three."""

import string

import pytest

# ruff: noqa: PLR2004
from questions.question_three import (
    check_multiple_string_equality,
    delete_random_character,
    equals_for_mutation,
    flip_random_character,
    generate_fuzzer_values,
    insert_random_character,
    mutate,
)


@pytest.mark.question_three_part_a
def test_mutate_functions_building_blocks():
    """Test for a question part."""
    # test delete_random_character function
    s = "hello"
    result = delete_random_character(s)
    assert len(result) == len(s) - 1, "delete_random_character failed: length mismatch"
    assert all(
        c in s for c in result
    ), "delete_random_character failed: unexpected characters"
    assert (
        delete_random_character("") == ""
    ), "delete_random_character failed: empty string case"
    # test insert_random_character function
    s = "world"
    result = insert_random_character(s)
    assert len(result) == len(s) + 1, "insert_random_character failed: length mismatch"
    assert all(
        c in string.printable for c in result
    ), "insert_random_character failed: non-printable character inserted"
    # test flip_random_character function
    s = "test"
    result = flip_random_character(s)
    assert len(result) == len(s), "flip_random_character failed: length mismatch"
    assert any(
        c != s[i] for i, c in enumerate(result)
    ), "flip_random_character failed: no character flipped"
    assert (
        flip_random_character("") == ""
    ), "flip_random_character failed: empty string case"


@pytest.mark.question_three_part_a
def test_overall_mutation_function():
    """Test for a question part."""
    # test mutate function with a non-empty string
    s = "example"
    result = mutate(s)
    assert len(result) in [
        len(s) - 1,
        len(s),
        len(s) + 1,
    ], "mutate failed: length invariant violated"
    assert all(
        c in string.printable for c in result
    ), "mutate failed: non-printable character in result"
    # test mutate function with an empty string
    s = ""
    result = mutate(s)
    assert (
        result == "" or len(result) == 1
    ), "mutate failed: empty string case invariant violated"
    assert all(
        c in string.printable for c in result
    ), "mutate failed: non-printable character in result for empty string"


@pytest.mark.question_three_part_b
def test_equals_for_strings():
    """Test for a question part."""
    # test case: equal strings
    assert equals_for_mutation(
        "hello", "hello"
    ), "equals failed: identical strings should be equal"
    # test case: different strings of same length
    assert not equals_for_mutation(
        "hello", "world"
    ), "equals failed: different strings of same length should not be equal"
    # test case: different strings of different lengths
    assert not equals_for_mutation(
        "hello", "helloo"
    ), "equals failed: strings of different lengths should not be equal"
    # test case: empty strings
    assert equals_for_mutation("", ""), "equals failed: empty strings should be equal"
    # test case: one empty string and one non-empty string
    assert not equals_for_mutation(
        "", "nonempty"
    ), "equals failed: empty string and non-empty string should not be equal"
    # test case: case sensitivity
    assert not equals_for_mutation(
        "Hello", "hello"
    ), "equals failed: strings with different cases should not be equal"


@pytest.mark.question_three_part_b
def test_equals_for_strings_after_mutation():
    """Test for a question part."""
    # test case: equal strings
    assert not equals_for_mutation(
        "hello", mutate("hello")
    ), "equals failed: identical strings should be equal"


@pytest.mark.question_three_part_c
def test_check_multiple_string_equality():
    """Test for a question part."""
    # test case: all strings equal to comparison string
    input_strings = ["test", "test", "test"]
    comparison_string = "test"
    result = check_multiple_string_equality(input_strings, comparison_string)
    assert all(
        result.values()
    ), "check_multiple_string_equality failed: all strings should be equal to comparison string"

    # test case: no strings equal to comparison string
    input_strings = ["test1", "test2", "test3"]
    comparison_string = "exemplify"
    result = check_multiple_string_equality(input_strings, comparison_string)
    assert not any(
        result.values()
    ), "check_multiple_string_equality failed: no strings should be equal to comparison string"
    # test case: empty strings
    input_strings = ["", ""]
    comparison_string = ""
    result = check_multiple_string_equality(input_strings, comparison_string)
    assert all(
        result.values()
    ), "check_multiple_string_equality failed: empty strings should be equal to empty comparison string"
    # test case: one empty string and one non-empty string
    input_strings = ["", "nonempty"]
    comparison_string = ""
    result = check_multiple_string_equality(input_strings, comparison_string)
    assert result[
        ""
    ], "check_multiple_string_equality failed: empty string should be equal to empty comparison string"
    assert not result[
        "nonempty"
    ], "check_multiple_string_equality failed: non-empty string should not be equal to empty comparison string"


@pytest.mark.question_three_part_d
def test_generate_fuzzer_values():
    """Confirm correctness of question part."""
    max_length = 10
    result = generate_fuzzer_values(max_length)
    assert len(result) <= max_length, "Generated string is too long"
    char_start = 65
    char_range = 26
    result = generate_fuzzer_values(100, char_start, char_range)
    for char in result:
        assert (
            char_start <= ord(char) < char_start + char_range
        ), "Character is not in range"
    result = generate_fuzzer_values(0)
    assert result == "", "Empty string not generated"
