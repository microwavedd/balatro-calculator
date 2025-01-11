from collections import Counter

"""jokersInGeneral = [joker,greedyjoker,lustyjoker,wrathfuljoker,gluttonousjoker,
                   jollyjoker,zanyjoker,madjoker,crazyjoker,drolljoker,
                   slyjoker,wilyjoker,cleverjoker,deviousjoker,craftyjoker,
                   halfjoker,jokerstencil,fourfingers,mime,creditcard,
                   ceremonialdagger,banner,mysticsummit,marblejoker,loyaltycard,
                   eightball,misprint,dusk,raisedfist,chaostheclown,
                   fibonacci,steeljoker,scaryface,abstractjoker,delayedgratification]"""

jokersInPlay,enhancementsInPlay,raritiesInPlay = [],[],[]
#Preliminary joker-related settings + intro
def pre():
    print(jokersInPlay,enhancementsInPlay,raritiesInPlay)
    addJoker = str(input(f"Which joker cards do you currently have active?\nYou can either add them separated with commas or one by one. \n If you re adding them the second way, type \"Done\" when you typed all of em' in.\n To add a joker, you need to type its name, if it has any bonus active and its rarity in that order. After typing every category, type a slash (/) to go to the next one\nYou currently have {len(jokersInPlay)} jokers in play.\n\n Type \"Tuto\" to get more information on how to introduce the info correctly.\n"))
    if addJoker.count("/") in (2,5,7,10,12,14):
        bits = addJoker.split("/")
        for i, part in enumerate(bits):
            if i % 3 == 0:
                jokersInPlay.append(part)
            elif i % 3 == 1:
                enhancementsInPlay.append(part)
            elif i % 3 == 2:
                raritiesInPlay.append(part)
    if addJoker.lower() == "tuto":
        print("\n\n\n\n\nJoker enhancements\n-------------------")
        print("In case of the joker having any of the specified enhancements, type the value to its right.\n")
        print("Base (standard card): X\nFoil (+50 chips): F\nHolo (+10 mult): H\nPolychrome (x1.5 mult): P\nNegative (Doesn't affect scored chips in any way: N)")
        print("\n\nJokes rarities\n-------------------")
        print("Type the rarity of the joker to the right of the enhancements.")
        print("Common: C\nUncommon: U\nRare: R\nLegendary: L")
        
        print("\n\nExample of usage\n-------------------")
        print("Example: faceLessJoker/P/C = Common rarity faceless joker with polychrome enhancement - (Example for adding one joker at a time).")
        print("\nExample 2: greenJoker/X/C,vampire/F/U, and so on. Note that if you add more than 5 jokers only the first 5 will be taken into account. You may introduce a lesser ammount than 5.")
        print("\nNote: The name of the joker doesn't need to be camel-cased, it can be typed anyhow as long as the full name is there with no whitespace.\n-------------------")
        input("Press enter to go back to the joker selection screen.\n")
        pre()

    confirm = str(input("\n\nDo you wish to add more jokers? (y/n)"))
    if confirm.lower() == "y":
        addJoker = ""
        pre()
    else:
        enterHand()
 
handChips,handMult = 0,0
cardRank,cardSuit,cardEnhancements,cardSeal = [],[],[],[]

#hand recognition algorithm:
def enterHand():
    addHand = str(input(f"What cards are you going to play?\nYou can insert them following the same instructions given in the joker section.\n To find instructions on how to know how to type a card can be found by typing \"tuto\".\n As it happened with the jokers, you may provide 5 cards at the same time sepparated by commas or one by one.\n"))
    if addHand.lower() == "tuto":
        pass
    if addHand.count("/") in (3,7,11,15,19):
        bits = addHand.split("/")
        for i, part in enumerate(bits):
            if i % 4 == 0:
                cardRank.append(part)
            elif i % 4 == 1:
                cardSuit.append(part)
            elif i % 4 == 2:
                cardEnhancements.append(part)
            elif i % 4 == 3:
                cardSeal.append(part)
    confirm = str(input("\n\nDo you wish to add more cards? (y/n)"))
    if confirm.lower() == "y":
        addHand = ""
        enterHand()
    else:
        pass
def whatHand(ranks,suits):
    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                   'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    rank_numbers = sorted([rank_values[rank] for rank in ranks])
    is_flush = len(set(suits)) == 1
    is_straight = all(rank_numbers[i] - rank_numbers[i - 1] == 1 for i in range(1, 5))
    
    if rank_numbers == [2, 3, 4, 5, 14]:
        is_straight = True
        rank_numbers = [1, 2, 3, 4, 5]
        
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
    