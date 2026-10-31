
import pytest

from scholarship_awards import (
    award_amount,
    is_eligible,
    application_status
)


# ==========================================
# BRANCH TESTS FOR award_amount()
# ==========================================

def test_unknown_category():
    with pytest.raises(ValueError):
        award_amount("science", 90, "low", False)


def test_negative_marks():
    with pytest.raises(ValueError):
        award_amount("merit", -5, "low", False)


def test_non_renewal_award():
    assert award_amount("merit", 80, "low", False) == 500


def test_renewal_non_sports():
    assert award_amount("arts", 70, "low", True) == 1000


def test_renewal_sports():
    assert award_amount("sports", 70, "high", True) == 600


def test_marks_at_cutoff():
    assert award_amount("merit", 75, "low", False) == 0


def test_marks_below_cutoff():
    assert award_amount("merit", 70, "low", False) == 0


def test_marks_above_cutoff():
    assert award_amount("merit", 80, "low", False) == 500


def test_marks_exactly_15_above_cutoff():
    assert award_amount("merit", 90, "low", False) == 1500


def test_marks_more_than_15_above_cutoff_low_income():
    assert award_amount("merit", 95, "low", False) == 3200


def test_marks_more_than_15_above_cutoff_high_income():
    assert award_amount("merit", 95, "high", False) == 2000


# ==========================================
# BRANCH TESTS FOR is_eligible()
# ==========================================

def test_special_quota_eligible():
    assert is_eligible(60, 2, True) is True


def test_special_quota_not_eligible():
    assert is_eligible(90, 3, True) is False


def test_attendance_below_75():
    assert is_eligible(74, 0, False) is False


def test_attendance_exactly_75():
    assert is_eligible(75, 0, False) is True


def test_normal_eligible():
    assert is_eligible(90, 1, False) is True


def test_normal_not_eligible():
    assert is_eligible(90, 2, False) is False


# ==========================================
# BRANCH TESTS FOR application_status()
# ==========================================

def test_regular_application_open():
    assert application_status(20, False, False) == "open"


def test_renewal_application_open():
    assert application_status(30, True, False) == "open"


def test_paper_application_open():
    assert application_status(30, False, True) == "open"


def test_renewal_paper_application_open():
    assert application_status(40, True, True) == "open"


def test_application_closing():
    assert application_status(10, False, False) == "closing"


def test_application_closing_at_boundary():
    assert application_status(5, False, False) == "closing"


def test_application_closed():
    assert application_status(4, False, False) == "closed"
