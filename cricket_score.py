import sys


def run_rate(runs, overs):
  if overs == 0:
    return 0
  return round(runs / overs, 2)


def strike_rate(runs, balls):
  if balls == 0:
    return 0
  return round((runs / balls) * 100, 2)


def required_rate(target, current_runs, remaining_overs):
  if remaining_overs == 0:
    return 0
  needed = target - current_runs
  return round(needed / remaining_overs, 2)


def match_status(target, current_runs):
  if current_runs >= target:
    return "Target Achieved"
  else:
    return "Chasing Target"


if __name__ == "__main__":
  runs = int(sys.argv[1])
  overs = float(sys.argv[2])
  batter_runs = int(sys.argv[3])
  balls = int(sys.argv[4])
  target = int(sys.argv[5])
  rem_overs = float(sys.argv[6])

  print("--- Cricket Score Summary ---")
  print("Current Run Rate :", run_rate(runs, overs))
  print("Strike Rate      :", strike_rate(batter_runs, balls))
  print("Required Run Rate:", required_rate(target, runs, rem_overs))
  print("Match Status     :", match_status(target, runs))