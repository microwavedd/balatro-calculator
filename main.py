from collections import Counter

"""jokersInGeneral = [joker,greedyjoker,lustyjoker,wrathfuljoker,gluttonousjoker,
                   jollyjoker,zanyjoker,madjoker,crazyjoker,drolljoker,
                   slyjoker,wilyjoker,cleverjoker,deviousjoker,craftyjoker,
                   halfjoker,jokerstencil,fourfingers,mime,creditcard,
                   ceremonialdagger,banner,mysticsummit,marblejoker,loyaltycard,
                   eightball,misprint,dusk,raisedfist,chaostheclown,
                   fibonacci,steeljoker,scaryface,abstractjoker,delayedgratification]"""
# Preliminary joker-related settings + intro
jokersInPlay, enhancementsInPlay, raritiesInPlay = [], [], []

def pre():
    print(jokersInPlay, enhancementsInPlay, raritiesInPlay)
    addJoker = input(
        f"Which joker cards do you currently have active?\n"
        f"You can either add them separated with commas or one by one.\n"
        f"If adding them the second way, type 'Done' when you're finished.\n"
        f"Type joker name/enhancement/rarity. Separate each joker by commas.\n"
        f"You currently have {len(jokersInPlay)} jokers in play.\n"
        f"Type 'Tuto' for more information.\n"
    )
    if addJoker.lower() == "tuto":
        print(
            "Joker enhancements:\n"
            "Base (standard card): X\nFoil (+50 chips): F\nHolo (+10 mult): H\n"
            "Polychrome (x1.5 mult): P\nNegative: N\n\n"
            "Joker rarities:\n"
            "Common: C\nUncommon: U\nRare: R\nLegendary: L\n"
        )
        pre()

    elif addJoker.lower() != "done":
        jokers = addJoker.split(",")
        for joker in jokers:
            bits = joker.split("/")
            if len(bits) == 3:
                jokersInPlay.append(bits[0])
                enhancementsInPlay.append(bits[1])
                raritiesInPlay.append(bits[2])
    
    confirm = input("Do you wish to add more jokers? (y/n): ")
    if confirm.lower() == "y":
        pre()
    else:
        enterHand()

# Hand-related settings
cardRank, cardSuit, cardEnhancements, cardSeal = [], [], [], []

def enterHand():
    addHand = input(
        "What cards are you going to play?\n"
        "Provide 5 cards separated by commas in the format rank/suit/enhancement/seal.\n"
        "Type 'Tuto' for instructions.\n"
    )
    if addHand.lower() == "tuto":
        print(
            "Example card format: A/H/F/C (Ace of Hearts, Foil enhancement, Common rarity)\n"
            "Separate cards by commas.\n"
        )
        enterHand()
    elif addHand.lower() != "done":
        cards = addHand.split(",")
        for card in cards:
            bits = card.split("/")
            if len(bits) == 4:
                cardRank.append(bits[0])
                cardSuit.append(bits[1])
                cardEnhancements.append(bits[2])
                cardSeal.append(bits[3])
    
    confirm = input("Do you wish to add more cards? (y/n): ")
    if confirm.lower() == "y":
        enterHand()
    else:
        handLevel()

def whatHand(ranks, suits):
    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                   '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    rank_numbers = sorted(rank_values[rank] for rank in ranks)
    is_flush = len(set(suits)) == 1
    is_straight = all(rank_numbers[i] - rank_numbers[i - 1] == 1 for i in range(1, 5))
    
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
    
playHand = whatHand(cardRank, cardSuit)
    
def levelScaler(hand):
    hands = ["High card","Pair","Two pair","Three of a kind","Four of a kind","Full house","Flush","Straight","Flush five","Flush house","Five of a kind", " Straight flush", "Royal flush"]
    chips = [5,10,20,30,60,40,35,30,160,140,120,100,100]
    mult = [1,2,2,3,7,4,4,4,16,14,12,8,8]
        
    index = hands.index(hand)
    return [chips[index],mult[index]]
pre()

handChips = levelScaler(playHand)[0]
handMult = levelScaler(playHand)[1]


def handLevel():

    addLevel = str(input(f"You are playing a {playHand}.\nWhat is the current level of the provided hand?\n"))
    return [handChips * addLevel, handMult * addLevel]

rank_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                   '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}


    
    

