import random
def roll_dice():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)
def simulate_dice_rolls(num_rolls):
    rolls = []
    for _ in range(num_rolls):
        dice_value = roll_dice()
        rolls.append(dice_value)
    return rolls
def play_against_computer():
    player_score = 0
    computer_score = 0
    while True:
        player_input = input("Press enter to roll the dice or 'q' to quit: ")
        if player_input.lower() == 'q':
            break
        player_value = roll_dice()
        computer_value = roll_dice()
        print("You rolled:", player_value)
        print("Computer rolled:", computer_value)
        if player_value > computer_value:
            player_score += 1
            print("You win this round!")
        elif player_value < computer_value:
            computer_score += 1
            print("Computer wins this round!")
        else:
         print("It's a tie!")
         print("Current Scores:")
         print("You:", player_score)
         print("Computer:", computer_score)
         print()
        print("Final Scores:")
        print("You:", player_score)
        print("Computer:", computer_score)
        print("Thank you for playing!")
def main():
    print("Welcome to the Advanced Dice Roll Simulator!")
    while True:
        user_input = input("Press enter to roll the dice, 'm' for multiple rolls,      'c' to play against the computer, or 'q' to quit: ")
        if user_input.lower() == 'q':
            print("Thank you for playing!")
            break
        elif user_input.lower() == 'm':
            num_rolls = int(input("Enter the number of rolls: "))
            rolls = simulate_dice_rolls(num_rolls)
            print("You rolled:", rolls)
        elif user_input.lower() == 'c':
            play_against_computer()
        else:
            dice_value = roll_dice()
            print("You rolled a", dice_value)
if __name__ == "__main__":
    main()
