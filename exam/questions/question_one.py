"""Question One: Executable Examination."""

# Note: The imports in the following source code block may no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

from typing import List

# Introduction: Read This First! {{{

# Keep in mind these considerations as you implement the required functions:

# --> You must implement Python functions to complete each of these steps,
# bearing in mind that one defective function may break another function.

# --> This may has functions that may be seeded with defects; this means
# that you will have to improve various aspects of this code to ensure
# that it passes the various tests and checks.

# --> Your source code must adhere to industry best practices in, for instance,
# source code formatting, variable naming, and documentation.

# --> You may refer to the checks that are specified in the exam/gatorgrade.yml
# file in this GitHub repository for the configuration and name of each tool
# used to analyze the code inside of this file.

# }}}

# Part (a) {{{

# Implement the following function(s) that perform an analysis of the test
# coverage data from more than one run of a test coverage monitoring tool.

# Function description:
# The function compute_coverage_intersection should:
# --> Take as input two lists of CoverageItem objects that represent the
#     coverage reports for a specific test run
# --> Return a list of CoverageItem objects that represent the coverage intersection
#     between the two coverage reports
# --> The coverage intersection is the set of CoverageItem objects that
#     have the same id and are covered in both coverage reports

# Function description:
# The function compute_coverage_difference should:
# --> Take as input two lists of CoverageItem objects that represent the
#     coverage reports for a specific test run
# --> Return a list of CoverageItem objects that represent the coverage difference
#     between the two coverage reports
# --> The coverage difference is the set of CoverageItem objects that
#     are present in the first coverage report but not in the second
#     coverage report, based on the id and covered status

# Note: These functions may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations so that the
# function and any code that uses it passes the type checker.

# Note: These functions may not have a docstring and thus it may not adhere to
# industry best practices for Python source code. You may need to add a
# docstring so that this function is correctly documented by an software
# engineer using it.

class CoverageItem:
    """A class to represent a coverage item."""

    def __init__(self, id: int, line: str, covered: bool):
        """Initialize the coverage item with the provided values."""
        self.id = id
        self.line = line
        self.covered = covered

    def __repr__(self):
        """Return a string representation of the coverage item."""
        return f"CoverageItem(id={self.id}, line='{self.line}', covered={self.covered})"

    def __str__(self):
        """Return a string representation of the coverage item."""
        return self.__repr__()


def compute_coverage_intersection(
    coverage_report_one: List[CoverageItem], coverage_report_two: List[CoverageItem]
) -> List[CoverageItem]:
    """Compute the coverage intersection between two coverage reports."""
    coverage_intersection = []
    return coverage_intersection


def compute_coverage_difference(
    coverage_report_one: List[CoverageItem], coverage_report_two: List[CoverageItem]
) -> List[CoverageItem]:
    """Compute the coverage difference between two coverage reports."""
    # initialize the coverage difference to be an empty list
    coverage_difference = []
    return coverage_difference


# }}}

# Part (b) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function calculate_coverage_score should:
# --> Take as input a list of CoverageItem objects that represent the coverage
#     report for a specific test run
# --> Return a float that represents the coverage score, which is defined
#     as the number of covered lines divided by the total number of items
#     in the coverage report
# --> If the coverage report is empty, the function should return 0.0 to
#     indicate that no items were covered when the tests were run

# Note: These functions may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations so that the
# function and any code that uses it passes the type checker.

# Note: These functions may not have a docstring and thus it may not adhere to
# industry best practices for Python source code. You may need to add a
# docstring so that this function is correctly documented by an software
# engineer using it.


def calculate_coverage_score(coverage_items: List[CoverageItem]) -> float:
    """Calculate the coverage score from a list of CoverageItem instances."""
    return 0.0


# }}}


# Part (c) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function compute_mutation_score should:
# --> Take as input a list of Mutant objects that represent the mutants created
#     by one or more mutation operators
# --> Return a float that represents the mutation score, which is defined
#     as the number of detected mutants divided by the total number of mutants
# --> The mutation score is defined to be 0.0 if no mutants were detected

# Note: Your implementation of this function should not modify the existing
# implementation of the Mutant class.

# Note: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


class Mutant:
    """A class to represent a mutant created by a mutation operator."""

    def __init__(self, id: int, line: str, detected: bool, equivalent: bool = False):
        """Initialize the coverage item with the provided values."""
        self.id = id
        self.line = line
        self.detected = detected
        self.equivalent = equivalent

    def __repr__(self):
        """Return a string representation of the mutant."""
        return f"Mutant(id={self.id}, line='{self.line}', detected={self.detected}, equivalent={self.equivalent})"

    def __str__(self):
        """Return a string representation of the coverage item."""
        return self.__repr__()


def compute_mutation_score(mutants):
    mutation_score = 0.0
    return mutation_score


# }}}

# Part (d) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function compute_mutation_score_equivalent_aware should:
# --> Take as input a list of Mutant objects that represent the mutants created
#     by one or more mutation operators
# --> Return a float that represents the mutation score, which is defined
#     as the number of detected mutants divided by the total number of mutants
# --> The mutation score is defined to be 0.0 if no mutants were detected
# --> Assume that some other tool (e.g., a static or dynamic analysis tool)
#     can determine that some mutants are equivalent to the original program
#     and thus should not be considered in the mutation score calculation
#     and thus must be ignored in both the numerator and the denominator
#     when computing the mutation score

# Note: This function should use the same implementation of the Mutant class that
# was defined and used for the previous part of this question.

# Note: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def compute_mutation_score_equivalent_aware(mutants):
    mutation_score = 0.0
    return mutation_score


# }}}
