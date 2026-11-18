from cricket_score import match_status, required_rate, run_rate, strike_rate


def test_run_rate():
  assert run_rate(120, 15) == 8.0
  assert run_rate(50, 0) == 0


def test_strike_rate():
  assert strike_rate(75, 50) == 150.0
  assert strike_rate(20, 0) == 0


def test_required_rate():
  assert required_rate(180, 140, 4) == 10.0


def test_match_status():
  assert match_status(180, 185) == "Target Achieved"
  assert match_status(180, 140) == "Chasing Target"