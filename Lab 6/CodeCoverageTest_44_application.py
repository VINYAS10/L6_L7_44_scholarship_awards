import pytest

from scholarship_awards import (
    award_amount,
    is_eligible,
    application_status
)


# ==========================================
# TEST CASES FOR award_amount()
# ==========================================

def test_unknown_category():
    with pytest.raises(ValueError):
        award_amount("science", 90, "low", False)


def test_negative_marks():
    with pytest.raises(ValueError):
        award_amount("merit", -5, "low", False)


def test_normal_low_income_award():
    assert award_amount("merit", 80, "low", False) == 500


def test_renewal_non_sports_award():
    assert award_amount("arts", 70, "low", True) == 1000


def test_sports_renewal_award():
    assert award_amount("sports", 70, "high", True) == 600


def test_high_excess_marks_low_income():
    assert award_amount("merit", 95, "low", False) == 3200


def test_high_excess_marks_other_income():
    assert award_amount("merit", 95, "high", False) == 2000


def test_marks_exactly_at_cutoff():
    assert award_amount("merit", 75, "low", False) == 0


# ==========================================
# TEST CASES FOR is_eligible()
# ==========================================

def test_special_quota_eligible():
    assert is_eligible(60, 2, True) is True


def test_special_quota_not_eligible():
    assert is_eligible(90, 3, True) is False


def test_low_attendance_not_eligible():
    assert is_eligible(70, 0, False) is False


def test_normal_eligible():
    assert is_eligible(85, 1, False) is True


def test_normal_not_eligible_due_to_backlogs():
    assert is_eligible(90, 2, False) is False


# ==========================================
# TEST CASES FOR application_status()
# ==========================================

def test_application_open():
    assert application_status(20, False, False) == "open"


def test_renewal_paper_application_open():
    assert application_status(40, True, True) == "open"


def test_application_closing():
    assert application_status(10, False, False) == "closing"


def test_application_closed():
    assert application_status(4, False, False) == "closed"