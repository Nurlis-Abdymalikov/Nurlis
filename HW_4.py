from random import randint, choice


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health}, damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes: list):
        random_hero: Hero = choice(heroes)
        self.__defence = random_hero.ability

    def attack(self, heroes: list):
        for hero in heroes:
            if hero.health > 0:
                if type(hero) == Berserk and self.defence != hero.ability:
                    hero.blocked_damage = choice([5, 10])
                    hero.health -= self.damage - hero.blocked_damage
                else:
                    hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super().__str__() + ' defence: ' + str(self.__defence)


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss: Boss):
        boss.health -= self.damage

    def apply_super_power(self, boss: Boss, heroes: list):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CRITICAL_DAMAGE')

    def apply_super_power(self, boss: Boss, heroes: list):
        crit = self.damage * randint(2, 5)
        print(f'Warrior {self.name} hit critically: {crit}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BOOSTING')
        self.active_boosts = {}

    def apply_super_power(self, boss: Boss, heroes: list):
        global round_number

        for hero, boost in self.active_boosts.items():
            hero.damage -= boost
        self.active_boosts.clear()

        boost = randint(10, 15)
        if round_number <= 4:
            for hero in heroes:
                if hero.health > 0:
                    hero.damage += boost
                    self.active_boosts[hero] = boost
        else:
            for hero in heroes:
                if hero in self.active_boosts:
                    hero.damage -= self.active_boosts[hero]
                    del self.active_boosts[hero]

class Hacker(Hero):
    def __init__(self,name,health, damage):
        super().__init__(name,health, damage,"HAKING")
    def apply_super_power(self, boss: Boss, heroes: list):
        global round_number
        if round_number % 2 == 0:
            hacking = randint(10,30)
            boss.health -= hacking
            target_hero = choice([hero for hero in heroes if hero.health > 0 and hero != self])
            target_hero.health += hacking
class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "NEW_LIFE")
        self.revived = False  # Флаг, чтобы воскрешать только один раз

    def apply_super_power(self, boss: Boss, heroes: list):
        if not self.revived:
            dead_heroes = [hero for hero in heroes if hero.health <= 0 and hero != self]
            if dead_heroes:
                target_hero = dead_heroes[0]
                target_hero.health = 100
                self.health = 0  #
                self.revived = True
                print(f"Witcher {self.name} revived {target_hero.name}!")

class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, 'HEAL')
        self.__heal_points = heal_points

    def apply_super_power(self, boss: Boss, heroes: list):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points

class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BLOCK_REVERT')
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss: Boss, heroes: list):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted: {self.__blocked_damage}')


round_number = 0


def show_statistics(boss: Boss, heroes: list):
    print(f'ROUND {round_number} ----------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_over(boss: Boss, heroes: list):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


def play_round(boss: Boss, heroes: list):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and boss.defence != hero.ability:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def start_game():
    boss = Boss('Splinter', 1000, 50)

    warrior_1 = Warrior('Django', 280, 10)
    warrior_2 = Warrior('Billy', 270, 15)
    magic = Magic('Dulittle', 290, 10)
    doc = Medic('James', 250, 5, 15)
    assistant = Medic('Marty', 300, 5, 5)
    berserk = Berserk('William', 260, 10)
    hac = Hacker('Adelina',260,5)
    wither = Witcher('Ali',300,0)

    heroes_list = [warrior_1, doc, warrior_2, magic, berserk, assistant, hac, wither]

    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)

start_game()
