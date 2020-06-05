"""
These tests are not really tests, they are just examples of using the pytest decorators to skip a test or mark it
as expected failure
"""
import pytest


@pytest.mark.skip
def test_this_will_not_run_because_it_is_marked_as_skip() -> None:
    assert False


@pytest.mark.xfail
def test_this_will_only_pass_when_the_assertion_fails() -> None:
    assert False
