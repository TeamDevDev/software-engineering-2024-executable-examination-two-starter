"""Confirm the correctness of functions in question_one."""

import pytest

# ruff: noqa: PLR2004
from questions.question_one import (
    CoverageItem,
    Mutant,
    calculate_coverage_score,
    compute_coverage_difference,
    compute_coverage_intersection,
    compute_mutation_score,
    compute_mutation_score_equivalent_aware,
)


@pytest.mark.question_one_part_a
def test_compute_coverage_difference():
    """Confirm correctness of question part."""
    item1 = CoverageItem(1, "line1", True)
    item2 = CoverageItem(2, "line2", True)
    item3 = CoverageItem(3, "line3", True)
    item4 = CoverageItem(4, "line4", True)
    item5 = CoverageItem(5, "line5", True)
    item6 = CoverageItem(6, "line6", True)
    item7 = CoverageItem(1, "line1", False)
    item8 = CoverageItem(2, "line2", False)
    item9 = CoverageItem(3, "line3", False)
    assert compute_coverage_intersection(
        [item1, item2, item3], [item1, item2, item3]
    ) == [
        item1,
        item2,
        item3,
    ], "Failed on case with identical coverage reports"
    assert (
        compute_coverage_intersection([item1, item2, item3], [item4, item5, item6])
        == []
    ), "Failed on case with no common coverage"
    assert compute_coverage_intersection(
        [item1, item2, item3], [item2, item3, item4]
    ) == [
        item2,
        item3,
    ], "Failed on case with partial overlap"
    assert compute_coverage_intersection(
        [item1, item2, item3], [item3, item2, item1]
    ) == [
        item1,
        item2,
        item3,
    ], "Failed on case with identical coverage reports in different order"
    assert (
        compute_coverage_intersection([], []) == []
    ), "Failed on case with empty coverage reports"
    assert (
        compute_coverage_intersection([item1, item2, item3], [item7, item8, item9])
        == []
    ), "Failed on case with same ids but not covered"
    assert (
        compute_coverage_difference([item1, item2, item3], [item1, item2, item3]) == []
    ), "Failed on case with identical coverage reports"
    assert compute_coverage_difference(
        [item1, item2, item3], [item4, item5, item6]
    ) == [
        item1,
        item2,
        item3,
    ], "Failed on case with no common coverage"
    assert compute_coverage_difference(
        [item1, item2, item3], [item2, item3, item4]
    ) == [item1], "Failed on case with partial overlap"
    assert (
        compute_coverage_difference([item1, item2, item3], [item3, item2, item1]) == []
    ), "Failed on case with identical coverage reports in different order"
    assert (
        compute_coverage_difference([], []) == []
    ), "Failed on case with empty coverage reports"
    assert compute_coverage_difference(
        [item1, item2, item3], [item7, item8, item9]
    ) == [
        item1,
        item2,
        item3,
    ], "Failed on case with same ids but different coverage status"


@pytest.mark.question_one_part_b
def test_compute_coverage_score():
    """Confirm correctness of question part."""
    # test with an empty list
    assert calculate_coverage_score([]) == 0.0, "Failed on empty list"
    # test with all items covered
    all_covered = [CoverageItem(1, "line1", True) for _ in range(5)]
    assert calculate_coverage_score(all_covered) == 1.0, "Failed on all items covered"
    # test with no items covered
    none_covered = [CoverageItem(1, "line1", False) for _ in range(5)]
    assert calculate_coverage_score(none_covered) == 0.0, "Failed on no items covered"
    # test with some items covered
    some_covered = [
        CoverageItem(1, "line1", True),
        CoverageItem(2, "line2", False),
        CoverageItem(3, "line3", True),
    ]
    assert (
        calculate_coverage_score(some_covered) == 2 / 3
    ), "Failed on some items covered"
    # test with one item covered
    one_covered = [CoverageItem(1, "line1", True)]
    assert calculate_coverage_score(one_covered) == 1.0, "Failed on one item covered"
    # test with one item not covered
    one_not_covered = [CoverageItem(1, "line1", False)]
    assert (
        calculate_coverage_score(one_not_covered) == 0.0
    ), "Failed on one item not covered"


@pytest.mark.question_one_part_c
def test_compute_mutation_score():
    """Confirm correctness of question part."""
    # summary of the checks:
    # check 1: Empty list of mutants
    # check 2: Empty
    # check 3: Partially detected
    # check 4: Fully detected
    # check 1: Empty list of mutants
    assert compute_mutation_score([]) == 0.0
    # check 2: All undetected mutants
    assert (
        compute_mutation_score([Mutant(1, "line1", False), Mutant(2, "line2", False)])
        == 0.0
    )
    # check 3: Partially detected mutants
    assert (
        compute_mutation_score([Mutant(1, "line1", True), Mutant(2, "line2", False)])
        == 0.5
    )
    # check 4: All detected mutants
    assert (
        compute_mutation_score([Mutant(1, "line1", True), Mutant(2, "line2", True)])
        == 1.0
    )


@pytest.mark.question_one_part_d
def test_compute_mutation_score_equivalent_aware():
    """Confirm correctness of question part."""
    # check 1: empty list of mutants
    assert compute_mutation_score_equivalent_aware([]) == 0.0
    # check 2: all undetected mutants that are not equivalent
    assert (
        compute_mutation_score_equivalent_aware(
            [Mutant(1, "line1", False, False), Mutant(2, "line2", False, False)]
        )
        == 0.0
    )
    # check 3: partially detected mutants that are not equivalent
    assert (
        compute_mutation_score_equivalent_aware(
            [Mutant(1, "line1", True, False), Mutant(2, "line2", False, False)]
        )
        == 0.5
    )
    # check 4: all detected mutants that are not equivalent
    assert (
        compute_mutation_score_equivalent_aware(
            [Mutant(1, "line1", True, False), Mutant(2, "line2", True, False)]
        )
        == 1.0
    )
    # check 5: equivalent mutants should be ignored
    assert (
        compute_mutation_score_equivalent_aware(
            [Mutant(1, "line1", True, True), Mutant(2, "line2", False, True)]
        )
        == 0.0
    )
    # check 6: mix of detected, undetected, and equivalent mutants
    assert (
        compute_mutation_score_equivalent_aware(
            [
                Mutant(1, "line1", True, False),
                Mutant(2, "line2", False, False),
                Mutant(3, "line3", True, True),
                Mutant(4, "line4", False, True),
            ]
        )
        == 0.5
    )
    # check 7: all of the mutants are equivalent
    assert (
        compute_mutation_score_equivalent_aware(
            [
                Mutant(1, "line1", True, True),
                Mutant(2, "line2", False, True),
                Mutant(3, "line3", True, True),
                Mutant(4, "line4", False, True),
            ]
        )
        == 0.0
    )
