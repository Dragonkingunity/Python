import random

# Player stats
p_Hp = 100
p_Mp = 50
p_Atk = 20
p_min_Atk = 5
p_Def = 10
p_Mdef = 5
p_speed = 100
p_Xp = 0
p_Level = 1

# Skills The player can learn as they level up
battle_Skills = {
    "Fire": {"mp_cost": 15, "damage": 30, "bouns": "burns the target", "next": "Firespear or lightning"},
    "Earth": {"mp_cost": 15, "damage": 30, "bouns": "slows the target", "next": "Earthspear"},
    "Water": {"mp_cost": 10, "damage": 20, "bouns": "heals 20 HP", "next": "waterspear"},
    "Wind": {"mp_cost": 5, "damage": 10, "bouns": "attacks 2 times", "next": "airspear"},
}
bskill_evolution = {
    "Firespear": {"mp_cost": 30, "damage": 50},
    "Lightning": {"mp_cost": 30, "damage": 50},

    "Earthspear": {"mp_cost": 30, "damage": 60},
    "waterspear": {"mp_cost": 40, "damage": 70},
    "airspear": {"mp_cost": 50, "damage": 80},
}
support_Skills = {
    "Shield": {"mp_cost": 20, "defense_boost": 10},
    "Heal": {"mp_cost": 15, "heal": 30},
}
sskill_evolution = {
    "Greater Shield": {"mp_cost": 40, "defense_boost": 20},
    "Greater Heal": {"mp_cost": 30, "heal": 60},
}

complete_Skills = {
    # All manipulations are passsive

    # basic manipulation skills that can be learned at certain levels
    "Fire Manipulation": {"Damage Boost": 50}, "next": "Fire Domination",
    "lightning Manipulation": {"Damage Boost": 50}, "next": "Lightning Domination",
    "Earth Manipulation": {"Slow Aura": -50}, "next": "Earth Domination",
    "Water Manipulation":  {"HP Boost": 200}, "next": "Water Domination",
    "Wind Manipulation": {"Speed Boost": 100}, "next": "Wind Domination",
    "Mana Manipulation": {"Mp Boost": 200}, "next": "Mana Domination",

    # combine certain manipulation skills to create powerful manipulations abilities
    "Gravity Manipulation": {"Slow Aura": -100, "Speed Boost": 200},# requires Earth Manipulation and Air Manipulation
    "Weather Manipulation": {"mp_cost": 120, "effect": "random weather effect"},# requires Water Manipulation and Air Manipulation and Fire Manipulation and Earth Manipulation
    "Molecule Manipulation": {"mp_cost": 200, "damage": 300},# requires all 4 manipulation skills
}

ultimate_Skills = {
    "Fire Domination": {"damage_boost": 50},
    "Lightning Domination": {"damage_boost": 50},
    "Earth Domination": {"slow aura": -50},
    "Water Domination":  {"heal": 200},
    "Wind Domination": {"speed_boost": 100},
    "Mana Domination": {"mp_boost": 200},

    "Gravity Domination": {"mp_cost": 100, "damage": 200},# requires Earth Domination and Air Domination
    "Time Domination": {"mp_cost": 150, "effect": "freeze time for 5 seconds"},# requires Air Domination and Fire Domination
    "Weather Domination": {"mp_cost": 120, "effect": "random weather effect"},# requires Water Domination and Air Domination and lightning Domination
    "Molecule Domination": {"mp_cost": 200, "damage": 300},# requires all 4 Domination skills
    ""
}

# Crate monster stages
stage_0 = ["Goblin", "Elf"]
stage_1 = ["Hobgoblin", "Wood Elf", "Wight"]
stage_2 = ["Ogre", "Dark Elf"]
stage_3 = ["Troll", "High Elf", "Wight King"]


# Monster progression
monster_progression = {
    "Goblin":      {"hp": 30,  "mp": 10,  "atk": 5, "minatk": 2, "speed": 100, "xp": 15,  "next": "Ogre"},
    "Hobgoblin":    {"hp": 50,  "mp": 30,  "atk": 10, "minatk": 5, "speed": 100, "xp": 20,  "next": "Orc"},
    "Ogre":         {"hp": 100, "mp": 50,  "atk": 25, "minatk": 10,"speed": 100, "xp": 30,  "next": "Troll"},
    "Troll":       {"hp": 150, "mp": 100, "atk": 35, "minatk": 15, "speed": 100, "xp": 50,  "next": "Goblin King"},
    "Goblin King": {"hp": 300, "mp": 150, "atk": 50, "minatk": 40, "speed": 150, "xp": 100, "next": None},
    "Elf":         {"hp": 40,  "mp": 30,  "atk": 10, "minatk": 5, "speed": 100, "xp": 25,  "next": "Wood Elf"},
    "Wood Elf":    {"hp": 60,  "mp": 60,  "atk": 15, "minatk": 10, "speed": 100, "xp": 40,  "next": "Dark Elf"},
    "Dark Elf":    {"hp": 80,  "mp": 100, "atk": 20, "minatk": 5, "speed": 100, "xp": 60,  "next": "High Elf"},
    "High Elf":    {"hp": 120, "mp": 150, "atk": 30, "minatk": 10, "speed": 100, "xp": 80,  "next": "Elf Queen"},
    "Elf Queen":   {"hp": 250, "mp": 300, "atk": 50, "minatk": 30, "speed": 300, "xp": 100, "next": None},
    "Wight":    {"hp": 20,  "mp": 100,   "atk": 5, "minatk": 2, "speed": 100, "xp": 20,  "next": "Wight King"},
    "Wight King":  {"hp": 50,  "mp": 300,   "atk": 10,"minatk": 5, "speed": 100, "xp": 50,  "next": "Lich"},
    "Lich":          {"hp": 100, "mp": 500, "atk": 20, "minatk": 10, "speed": 200, "xp": 100,  "next": None},
}

monster_list = ["Goblin", "Ogre", "Orc", "Troll", "Elf", "Wood Elf", "Dark Elf", "High Elf", "Wight", "Wight King"]
boss_list = ["Goblin King", "Elf Queen", "Lich"]

def level_up():
    global p_Hp, p_Mp, p_Atk, p_min_Atk, p_Xp, p_Level  
    p_Level += 1
    p_Hp = 100 + (p_Level - 1) * 20  
    p_Mp += 10 + (p_Level - 1) * 20
    p_Atk += 10
    p_min_Atk += 5
    p_Xp = 0
    print(f"\n*** LEVEL UP! You are now Level {p_Level}! ***")
    print(f"HP: {p_Hp} | MP: {p_Mp} | ATK: {p_min_Atk}-{p_Atk}")

def battle(current_monster):
    global p_Hp, p_Xp

    stats = monster_progression[current_monster]
    m_Hp = stats["hp"]
    m_Mp = stats["mp"]
    m_Atk = stats["atk"]
    m_Xp = stats["xp"]
    next_monster = stats["next"]

    print(f"\n--- A {current_monster} appears! ---")
    print(f"Monster HP: {m_Hp} | MP: {m_Mp} | ATK: {m_Atk}")

    for turn in range(1, 6):
        print(f"\n-- Turn {turn} --")

        p_damage = random.randint(p_min_Atk, p_Atk)
        m_Hp -= p_damage
        print(f"You deal {p_damage} damage! Monster HP: {max(m_Hp, 0)}")

        m_damage = random.randint(1, m_Atk)
        p_Hp -= m_damage
        print(f"{current_monster} deals {m_damage} damage! Your HP: {max(p_Hp, 0)}")

        if m_Hp <= 0:
            p_Xp += m_Xp
            print(f"\nYou defeated the {current_monster}! +{m_Xp} XP | Total XP: {p_Xp}/100")
            if p_Xp >= 100:
                level_up()
            return current_monster

        if p_Hp <= 0:
            print("\nYou have been defeated!")
            return None

    print(f"\nThe {current_monster} survived!")
    if next_monster:
        print(f"The {current_monster} evolved into a {next_monster}!")
        return next_monster
    else:
        print(f"The {current_monster} is already at max power!")
        return current_monster


# --- Game loop ---
goblin_count = 0
elf_count = 0
current_monster = "Goblin"

while True:
    print(f"\n== Player Level: {p_Level} | HP: {p_Hp} | MP: {p_Mp} | ATK: {p_min_Atk}-{p_Atk} | XP: {p_Xp}/100 ==")

    result = battle(current_monster)

    if result is None:
        print(f"\n--- GAME OVER ---")
        print(f"You reached Level {p_Level} before being defeated!")
        break

    if current_monster == "Goblin" and goblin_count < 5:
        goblin_count += 1

    if current_monster == "Elf" and elf_count < 5:
        elf_count += 1

    if goblin_count < 5:
        print(f"\nAnother Goblin approaches! ({goblin_count}/5)")
        current_monster = "Goblin"
    elif goblin_count == 5 and elf_count == 0:
        print(f"\nYou defeated 5 Goblins! The Elves emerge from the forest...")
        current_monster = "Elf"
    elif elf_count < 5:
        print(f"\nAnother Elf approaches! ({elf_count}/5)")
        current_monster = "Elf"
    elif elf_count == 5 and result == "Elf":
        print(f"\nYou defeated 5 Elves! Stronger monsters await...")
        current_monster = random.choice(monster_list)
    else:
        current_monster = result

    input("\nPress Enter to continue...")