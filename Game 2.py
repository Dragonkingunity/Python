import random

# Player stats
p_Hp = 100
p_Mp = 50
p_Atk = 20
p_min_Atk = 5  # ✅ added minimum attack
p_Xp = 0
p_Level = 1

# Monster progression
monster_progression = {
    "Goblin":      {"hp": 30,  "mp": 10,  "atk": 5,  "xp": 20,  "next": "Ogre"},
    "Ogre":        {"hp": 50,  "mp": 30,  "atk": 10, "xp": 35,  "next": "Orc"},
    "Orc":         {"hp": 100, "mp": 50,  "atk": 25, "xp": 50,  "next": "Troll"},
    "Troll":       {"hp": 150, "mp": 100, "atk": 35, "xp": 70,  "next": "Goblin King"},
    "Goblin King": {"hp": 200, "mp": 150, "atk": 50, "xp": 100, "next": None},
}

monster_list = ["Goblin", "Ogre", "Orc", "Troll"]
boss_list = ["Goblin King", "Elf Queen"]

def level_up():
    global p_Mp, p_Atk, p_min_Atk, p_Xp, p_Level
    p_Level += 1
    p_Mp += 10
    p_Atk += 10
    p_min_Atk += 5  # ✅ boost minimum damage on level up
    p_Xp = 0
    print(f"\n*** LEVEL UP! You are now Level {p_Level}! ***")
    print(f"MP: {p_Mp} | ATK: {p_min_Atk}-{p_Atk}")

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

    for turn in range(1, 4):
        print(f"\n-- Turn {turn} --")

        p_damage = random.randint(p_min_Atk, p_Atk)  # ✅ uses p_min_Atk
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

    if goblin_count < 5:
        print(f"\nAnother Goblin approaches! ({goblin_count}/5)")
        current_monster = "Goblin"
    elif goblin_count == 5 and result == "Goblin":
        print(f"\nYou defeated 5 Goblins! Stronger monsters await...")
        current_monster = random.choice(monster_list)
    else:
        current_monster = result

    input("\nPress Enter to continue...")