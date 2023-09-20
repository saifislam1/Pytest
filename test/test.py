import pytest
from pytest_bdd import scenarios, given, when, then

scenarios('Feature.feature')

@given('I have the numbers 5 and 7')
def input_numbers():
    return [5, 7]

@when('I add these numbers')
def add_numbers(input_numbers):
    return sum(input_numbers)

@then('I get the result 12')
def check_result(add_numbers):
    assert add_numbers == 12
