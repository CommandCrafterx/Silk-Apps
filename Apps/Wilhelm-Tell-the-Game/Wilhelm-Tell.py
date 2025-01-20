import random

class Character:
    def __init__(self, name, hp, attack, abilities):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.abilities = abilities

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def use_ability(self, ability, target):
        if ability.damage > 0:
            print(f"{self.name} uses {ability.name} on {target.name}")
            target.take_damage(ability.damage)
        if ability.heal > 0:
            print(f"{self.name} uses {ability.name} to heal")
            self.hp += ability.heal
            if self.hp > self.max_hp:
                self.hp = self.max_hp
        if ability.defense > 0:
            print(f"{self.name} uses {ability.name} to defend")
            self.defense = True

class Ability:
    def __init__(self, name, damage=0, heal=0, defense=False):
        self.name = name
        self.damage = damage
        self.heal = heal
        self.defense = defense

def battle(player, enemies):
    turn = 0
    while player.is_alive() and any(enemy.is_alive() for enemy in enemies):
        print(f"\n-- Turn {turn + 1} --")
        print(f"Player HP: {player.hp}/{player.max_hp}")
        if turn % 2 == 0:
            # Player's turn
            action = input("Choose an action (attack/ability): ").strip().lower()
            if action == "attack":
                target = random.choice([enemy for enemy in enemies if enemy.is_alive()])
                print(f"Wilhelm Tell attacks {target.name}")
                target.take_damage(player.attack)
            elif action == "ability":
                for i, ability in enumerate(player.abilities):
                    print(f"{i + 1}. {ability.name}")
                choice = int(input("Choose an ability: ")) - 1
                if 0 <= choice < len(player.abilities):
                    ability = player.abilities[choice]
                    target = random.choice([enemy for enemy in enemies if enemy.is_alive()]) if ability.damage > 0 else player
                    player.use_ability(ability, target)
        else:
            # Enemies' turn
            for enemy in enemies:
                if enemy.is_alive():
                    print(f"{enemy.name} attacks Wilhelm Tell")
                    player.take_damage(enemy.attack)
        turn += 1

    if player.is_alive():
        print("Wilhelm Tell has won the battle!")
    else:
        print("Wilhelm Tell has been defeated.")

def main_story():
    print("Welcome to the story of Wilhelm Tell!")
    print("Wilhelm Tell must fight against the tyrannical ruler and his army to free his people.")
    print("Each battle brings him closer to his goal, but the enemies become stronger as he progresses.")

    # Introduction sequence
    print("\nOnce upon a time in Switzerland, a brave man named Wilhelm Tell stood against tyranny.")
    input("Press Enter to continue...")

    # Example characters
    player = Character("Wilhelm Tell", 150, 25, [
        Ability("Arrow Shot", 40),
        Ability("Sword Slash", 30),
        Ability("Heal", heal=50),
        Ability("Explosive Arrow", damage=20),
        Ability("Defend", defense=True),
        Ability("Power Strike", damage=50)
    ])

    levels = [
        {
            "enemies": [
                Character("Soldier", 30, 5, []),
                Character("Archer", 25, 7, [])
            ],
            "story": "Wilhelm Tell encounters a small group of soldiers blocking his path."
        },
        {
            "enemies": [
                Character("Elite Soldier", 50, 10, []),
                Character("Lieutenant", 70, 12, [])
            ],
            "story": "As Wilhelm advances, he faces the elite guards of the tyrant."
        }
    ]

    for i, level in enumerate(levels):
        print(f"\n--- Level {i + 1} ---")
        print(level["story"])
        input("Press Enter to continue...")
        battle(player, level["enemies"])
        if not player.is_alive():
            print("Game Over!")
            break

    if player.is_alive():
        print("Congratulations! Wilhelm Tell has freed his people!")

if __name__ == "__main__":
    main_story()