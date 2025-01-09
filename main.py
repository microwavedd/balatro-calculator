
jokersInGeneral = [joker,greedyjoker,lustyjoker,wrathfuljoker,gluttonousjoker,
                   jollyjoker,zanyjoker,madjoker,crazyjoker,drolljoker,
                   slyjoker,wilyjoker,cleverjoker,deviousjoker,craftyjoker,
                   halfjoker,jokerstencil,fourfingers,mime,creditcard,
                   ceremonialdagger,banner,mysticsummit,marblejoker,loyaltycard,
                   eightball,misprint,dusk,raisedfist,chaostheclown,
                   fibonacci,steeljoker,scaryface,abstractjoker,delayedgratification]
jokersInPlay = []
#Preliminary joker-related settings + intro
def pre():
    addJoker = str(input("Which joker cards do you currently have active?\nYou can either add them separated with commas or one by one. \n If you re adding them the second way, type \"Done\" when you typed all of em' in.\n To add a joker, you need to type its name, if it has any bonus active and its rarity in that order. After typing every category, type a slash (/) to go to the next one.\n Type \"Transcript\" to get more information on how to introduce the info correctly.\n"))
    if addJoker.lower() == "transcript":
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
pre()        