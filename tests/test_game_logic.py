from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


def test_winning_guess():
    outcome, _message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_easy_range_is_1_to_20():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_hard_range_is_harder_than_normal():
    _normal_low, normal_high = get_range_for_difficulty("Normal")
    _hard_low, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high


def test_parse_guess_blank_is_invalid():
    ok, value, err = parse_guess("   ")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."


def test_parse_guess_float_string_gets_cast_to_int():
    ok, value, err = parse_guess("42.9")
    assert ok is True
    assert value == 42
    assert err is None


def test_score_penalty_for_non_win_outcomes():
    assert update_score(20, "Too High", 1) == 15
    assert update_score(20, "Too Low", 2) == 15


def test_win_score_has_floor():
    # Very late win should still award at least 10 points.
    assert update_score(0, "Win", 20) == 10
