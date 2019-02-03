import random

def get_user():
    user_name = ""
    user_name = input("How do you call yourself?")
    return user_name

def greet_user(heros_name):
    print("Greetings", heros_name + "! My name is Thrognor, I run this game.")
    print("All adventurers start with 15 health in my game and you're no different")
    print("Keep in mind my monsters aren't adventurers, some have more health and some have less")
    print("So be careful out there!")
    print("If you can survive 6 adventures then the coins you've found are yours, GOOD LUCK!")
    print("")

def validate_string(string):
    if string == "Y" or string == "N":
        return True
    else:
        print("Sorry we only accept y or n as of now")
        print("")
        return False

def monster_array():
    monsters = []
    monsters = [["Goblin","Kobold","Wolf"], ["Worg","Dire Owlbear","High Summoner of Gruumsh"], ["Black Dragon", "Beholder", "Lich"]]
    return monsters

def determine_column():
    column = 0
    column = random.randint(0, 2)
    return column

def determine_row():
    row = 0
    row = random.randint(0, 2)
    return row

def who_are_you_fighting(column, row, monster_array):
    monster = ""
    monster = monster_array[row][column]
    print("Oh No! it look's like you've found a", monster)
    return monster

def shall_we_battle(m_health, hero_health):
    if m_health > 0 and hero_health > 0:
        return True
    else:
        return False

def heros_attack_choice():
    attack_choice = ""
    attack_choice = input("Normal or Special?").upper()
    while not(validate_attack(attack_choice)):
        print("How do you want to attack?")
        attack_choice = input("Normal or Special?").upper()
    return attack_choice

def validate_attack(string):
    if string == "SPECIAL" or string == "NORMAL":
        return True
    else:
        print("Hmm didn't catch that Boss, one more time for the hard of hearing")
        print("")
        return False

def monsters_health(row):
    health = 0
    if row == 2:
        health = random.randint(1,15)
        health = health +10
        return health
    elif row == 1:
        health = random.randint(1,12)
        health = health + 6
        return health
    else:
        health = random.randint(1,8)
        health = health + 4
        return health

def monster_damage(row):
    m_damage = 0
    if row == 2:
        m_damage = random.randint(1,8)
        m_damage = int((m_damage * 3)/2)
        return m_damage
    elif row == 1:
        m_damage = random.randint(1,8)
        m_damage = int((m_damage * 2))
        return m_damage
    else:
        damage = random.randint(1,8)
        return damage

def heros_damage(choice):
    damage = 0
    if choice == "NORMAL":
        damage = random.randint(1,8)+2
        print_damage(damage)
        return damage
    elif choice == "SPECIAL":
        damage = 2 * random.randint(1,8)+5
        print_damage(damage)
        return damage
    else:
        print("Hmm something has gone wrong here")

def print_damage(damage):
    print("You've dealt", damage, "damage to the beast")

def heros_attack(m_health, choice):
    damage = heros_damage(choice)
    m_health = m_health - damage
    print("The vile beast is at", m_health, "health")
    print ("")
    return m_health

def get_new_monster(row, column):
    current_monster = ""
    current_monster = who_are_you_fighting(row, column)
    print("Oh No! it look's like you've found a", current_monster)
    return current_monster

def monster_feedback(m_health, name, current_monster):
    if m_health <= 10:
        print("I wouldn't be too worried, it looks like a weakling")
    elif m_health <= 13:
        print("I don't know,", name + ", that", current_monster, "looks pretty tough")
    else:
        print("AHH!", name.upper(), "THAT THING IS HUGE!")

def adventure_counter(m_health, adventures):
    if m_health <= 0:
        adventures += 1
        return adventures

def special_counter(choice,special):
    if choice == "SPECIAL":
        special += 1
        if special > 1:
            print_special()
            special = 2
            return special
        return special
    else:
        return special

def print_special():
    print("")
    print("You look exhausted, save your energy")
    print("You'll need to use Normal attacks until your energy is back up")
    print("")

def loot(row):
    coins = 0
    if row == 2:
        coins = random.randint(1,8)
        coins = int(coins * 4)
        return coins
    elif row == 1:
        coins = random.randint(1,8)
        coins = int(coins * 2)
        return coins
    else:
        coins = random.randint(1,8)
        return coins

def print_loot(coins):
    if coins == 1:
        print("You've found", coins, "coin")
    else:
        print("You've found", coins, "coins")

def adventure_counter(adventures):
    adventures += 1
    if adventures > 0:
        if adventures == 1:
            print("You've gone on", adventures, "adventure")
        else:
            print("You've gone on", adventures, "adventures")
    return adventures

def loot_haul(coins, total_haul):
    total_haul += coins
    print("You have", total_haul, "total coins")
    print("")
    return total_haul

def attack(choice, special, m_health):
    while choice != "NORMAL" and special > 1:
        choice = heros_attack_choice()
        if choice == "SPECIAL":
            special += 1
    m_health = heros_attack(m_health, choice)
    return m_health

def so_youve_died(name, adventures, coins):
    print("You're dead", name + "!")
    print("Better luck next time")
    print("You went on", adventures, "adventures")
    print("You died with", coins, "coins")

def youve_won(name, coins):
    print("WOW", name, "you did it! You went on 6 adventures, very impressive!")
    print("You managed to amass", coins, "coins")

def adventure_on(adventures, death):
    if adventures < 6 and death == 0:
        return True
    else:
        return False

def want_to_play_a_game(counter):
    go_again = ""
    if counter >= 1:
        go_again = input("Would you like to play again? (y/n)").upper()
        while not (validate_string(go_again)):
            go_again = input("Would you like to play again? (y/n)").upper()
        if go_again == "N":
            print("Hope you had fun")
    else:
        go_again = input("Are you brave enough to venture out? (y/n)").upper()
        while not (validate_string(go_again)):
            go_again = input("Are you brave enough to venture out? (y/n)").upper()
        if go_again == "N":
            print("Well adventuring isn't for everyone!")
    print("")
    return go_again

def end_of_journey(death, adventures, name, coins):
    if death == 1:
        so_youve_died(name, adventures, coins)
        print("")
    if adventures == 6:
        youve_won(name, coins)
        print("")

def location_array():
    locations = [""] * 8
    locations = ["an old bear's cave", "a piranha infested lake", "a spirit imbued forest", "Tobias Fuenke's Magical Wizard's Tower",
                 "the Minotaur's Endless Maze", "Isengard's renowned, decrepit sewers", "the Forgotten Desert", "a heavy fog ridden swamp"]
    return locations

def get_location(location_array):
    element = 0
    location = ""
    element = random.randint(0,len(location_array)-1)
    location = location_array[element]
    print("In your travels, you've come across", location + ". I wonder what we can find in there")

def main():
    row = 0
    column = 0
    monster_health = 0
    hero_health = 0
    m_damage = 0
    temp_loot = 0
    counter = 0
    location = ""
    choice = ""
    current_monster = ""
    name = get_user()
    while want_to_play_a_game(counter)== "Y":
        adventures = 0
        death = 0
        coins = 0
        hero_health = 15
        special = 0
        while adventure_on(adventures, death):
            counter = 1
            row = determine_row()
            column = determine_column()
            location = get_location(location_array())
            current_monster = who_are_you_fighting(column, row, monster_array())
            m_health = monsters_health(row)
            monster_feedback(m_health, name, current_monster)
            while shall_we_battle(m_health, hero_health):
                choice = heros_attack_choice()
                special = special_counter(choice, special)
                m_health = attack(choice, special, m_health)
                if m_health <= 0:
                    adventures = adventure_counter(adventures)
                    hero_health += 5
                    print("Rest up for a second,", name)
                    print (name, "is now at", hero_health, "health")
                    temp_loot = loot(row)
                    print_loot(temp_loot)
                    coins = loot_haul(temp_loot, coins)
                elif hero_health >= 0:
                    m_damage = monster_damage(row)
                    print("The", current_monster, "dealt",m_damage, "damage")
                    hero_health = hero_health - m_damage
                    print("you're at", hero_health, "health")
                    print("")
                if hero_health <= 0:
                    death = 1
            end_of_journey(death, adventures, name, coins)



main()