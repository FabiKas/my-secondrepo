from character import Character

def main():
    hero = Character("Knight", 30, 5)
    enemies = [
        Character("Goblin", 20, 3),
        Character("Orc", 25, 4)
    ]

    print(hero)
    print()

    for enemy in enemies:
        print(f"A wild {enemy.name} appears!")
        print(enemy)
        print()

        while hero.is_alive() and enemy.is_alive():
            hero.attack(enemy)
            if enemy.is_alive():
                enemy.attack(hero)
            print(hero)
            print(enemy)
            print()

        if not hero.is_alive():
            print("Battle over!")
            print(f"{enemy.name} wins!")
            return 

        print(f"{enemy.name} is defeated!\n")

    print("All enemies defeated!")
    print(f"{hero.name} wins!")

if __name__ == "__main__":
    main()
