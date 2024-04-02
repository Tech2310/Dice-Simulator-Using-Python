import random

def roll_dice(num_dice, num_sides):
  """
  Simulates rolling a specified number of dice with a specified number of sides.

  Args:
      num_dice: The number of dice to roll.
      num_sides: The number of sides on each die.

  Returns:
      A list of the results of each die roll.
  """
  rolls = []
  for _ in range(num_dice):
    rolls.append(random.randint(1, num_sides))
  return rolls

# Example usage
while True:
  num_dice = int(input("How many dice do you want to roll? "))
  num_sides = int(input("How many sides are on each die? "))

  dice_rolls = roll_dice(num_dice, num_sides)

  print(f"You rolled {num_dice} dice with {num_sides} sides and got:")
  for roll in dice_rolls:
    print(roll)

  roll_again = input("Roll again? (y/n): ")
  if roll_again.lower() != "y":
    break

print("Thanks for playing!")
