from collections import Counter

"""jokersInGeneral = [joker,greedyjoker,lustyjoker,wrathfuljoker,gluttonousjoker,
                   jollyjoker,zanyjoker,madjoker,crazyjoker,drolljoker,
                   slyjoker,wilyjoker,cleverjoker,deviousjoker,craftyjoker,
                   halfjoker,jokerstencil,fourfingers,mime,creditcard,
                   ceremonialdagger,banner,mysticsummit,marblejoker,loyaltycard,
                   eightball,misprint,dusk,raisedfist,chaostheclown,
                   fibonacci,steeljoker,scaryface,abstractjoker,delayedgratification]"""
# Preliminary joker-related settings + intro
# Global variables for jokers, enhancements, and hand-related settings
jokers_in_play, enhancements_in_play, rarities_in_play = [], [], []
play_hand = []

# Joker-related settings + intro
def pre():
    print("Welcome to the Joker Card Setup!")
    print("Current Jokers in play:", jokers_in_play)

    while True:
        add_joker = input(
            "\nWhich joker cards do you currently have active?\n"
            "Provide joker/enhancement/rarity separated by commas, or type 'Done' to finish.\n"
            "Type 'Tuto' for instructions.\n"
        )
        if add_joker.lower() == "tuto":
            print(
                "\nJoker enhancements:\n"
                "- Base (standard card): X\n"
                "- Foil (+50 chips): F\n"
                "- Holo (+10 mult): H\n"
                "- Polychrome (x1.5 mult): P\n"
                "- Negative: N\n\n"
                "Joker rarities:\n"
                "- Common: C\n"
                "- Uncommon: U\n"
                "- Rare: R\n"
                "- Legendary: L\n"
            )
            continue

        if add_joker.lower() == "done":
            break

        jokers = add_joker.split(",")
        for joker in jokers:
            bits = joker.strip().split("/")
            if len(bits) == 3:
                jokers_in_play.append(bits[0].strip())
                enhancements_in_play.append(bits[1].strip())
                rarities_in_play.append(bits[2].strip())
            else:
                print(f"Invalid joker format: {joker}. Please try again.")

    print("\nJoker setup complete.")
    enter_hand()

# Hand-related settings
def enter_hand():
    global play_hand
    print("\nLet's configure your hand of cards.")

    while True:
        add_hand = input(
            "\nWhat cards are you going to play?\n"
            "Provide up to 5 cards in the format rank/suit/enhancement/seal separated by commas.\n"
            "Type 'Done' when finished or 'Tuto' for instructions.\n"
        )
        if add_hand.lower() == "tuto":
            print(
                "\nExample card format: A/H/F/C\n"
                "(Ace of Hearts, Foil enhancement, Common rarity)\n"
                "Separate cards by commas.\n"
            )
            continue

        if add_hand.lower() == "done":
            break

        cards = add_hand.split(",")
        for card in cards:
            bits = card.strip().split("/")
            if len(bits) == 4:
                card_rank.append(bits[0].strip())
                card_suit.append(bits[1].strip())
                card_enhancements.append(bits[2].strip())
                card_seal.append(bits[3].strip())
            else:
                print(f"Invalid card format: {card}. Please try again.")

        if len(card_rank) >= 5:
            print("Maximum of 5 cards allowed. Proceeding with evaluation.")
            break

    play_hand = determine_hand(card_rank, card_suit)
    calculate_rewards(play_hand)

# Determine the type of poker hand
def determine_hand(ranks, suits):
    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                   '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    rank_numbers = sorted(rank_values[rank] for rank in ranks)
    is_flush = len(set(suits)) == 1
    is_straight = all(rank_numbers[i] - rank_numbers[i - 1] == 1 for i in range(1, len(rank_numbers)))

    if rank_numbers == [2, 3, 4, 5, 14]:
        is_straight = True

    rank_counts = Counter(rank_numbers)
    counts = sorted(rank_counts.values(), reverse=True)

    if is_straight and is_flush:
        return "Royal Flush" if max(rank_numbers) == 14 else "Straight Flush"
    elif counts == [4, 1]:
        return "Four of a Kind"
    elif counts == [3, 2]:
        return "Full House"
    elif is_flush:
        return "Flush"
    elif is_straight:
        return "Straight"
    elif counts == [3, 1, 1]:
        return "Three of a Kind"
    elif counts == [2, 2, 1]:
        return "Two Pair"
    elif counts == [2, 1, 1, 1]:
        return "One Pair"
    else:
        return "High Card"

# Calculate rewards based on hand type
def calculate_rewards(hand):
    hand_data = {
        "High Card": {"chips": 5, "mult": 1},
        "One Pair": {"chips": 10, "mult": 2},
        "Two Pair": {"chips": 20, "mult": 2},
        "Three of a Kind": {"chips": 30, "mult": 3},
        "Straight": {"chips": 40, "mult": 4},
        "Flush": {"chips": 35, "mult": 4},
        "Full House": {"chips": 50, "mult": 5},
        "Four of a Kind": {"chips": 60, "mult": 7},
        "Straight Flush": {"chips": 100, "mult": 10},
        "Royal Flush": {"chips": 200, "mult": 20},
    }

    if hand not in hand_data:
        print("Invalid hand type. No rewards calculated.")
        return

    chips = hand_data[hand]["chips"]
    mult = hand_data[hand]["mult"]

    level = int(input(f"\nYou are playing a {hand}. Enter the level of your hand (1 or higher): "))

    total_chips = chips * level
    total_mult = mult * level

    print(f"\nFinal Results:\nHand: {hand}\nChips: {total_chips}\nMultiplier: {total_mult}\nTotal Reward: {total_chips * total_mult}")

# Run the program
if __name__ == "__main__":
    card_rank, card_suit, card_enhancements, card_seal = [], [], [], []
    pre()
