import random

def biased_dice_roll():
  """Simulates a dice roll with a guaranteed 6.

  Returns:
      int: Always 6.
  """

  # Force the outcome to be 6
  return 6

# Simulate a few dice rolls
for _ in range(5):
  result = biased_dice_roll()
  print(f"Rolled: {result}")
