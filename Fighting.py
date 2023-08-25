import random
import keyboard
import os
import colorama
cyan = colorama.Fore.CYAN
blue = colorama.Fore.BLUE
def clear(): return os.system('cls')


role = {
    '1': 'Warrior',
    '2': 'Ranger',
    '3': 'Mage',
    '4': 'Healer',
    '5': 'Assasin'
}
classes = {
    'Warrior': {
        'hp': 75,
        'attack': 13,
        'armor': 8,
        'uses': {
            'shield': {
                'power': 1,
                'kd': 0
            }
        }
    },
    'Ranger': {
        'hp': 55,
        'attack': 14,
        'armor': 8,
        'uses': {
            'xhit': {
                'power': 1,
                'kd': 0
            }
        }
    },
    'Mage': {
        'hp': 53,
        'attack': 5,
        'armor': 9,
        'uses': {
            'fireball': {
                'power': 12,
                'kd': 0
            }
        }
    },
    'Healer': {
        'hp': 65,
        'attack': 13,
        'armor': 7,
        'uses': {
            'heal': {
                'power': 11,
                'kd': 0
            }
        }
    },
    'Assasin': {
        'hp': 48,
        'attack': 15,
        'armor': 6,
        'uses': {
            'crit': {
                'power': 1.2,
                'chance': 25
            }
        }
    }
}
second_name = ['слесарь', 'мухомор', 'пепел', 'лемур', 'шаман', 'пельмень', 'слизень', 'алхимик', 'крот', 'фикус',
               'кролик', 'танцор', 'пингвин', 'викинг', 'паук', 'плащ', 'мексиканец']
first_name = ['Доктор', 'Летающий', 'Профессор', 'Скучный', 'Мега', 'Железный', 'Голодный', 'Капитан', 'Быстрый',
              'Мистер', 'Горячий', 'Звездный', 'Космический', 'Просто', 'Восхитительный', 'Непобедимый']


def init_person(is_enemy: bool) -> dict[str, str | dict[str, int | dict]]:
    if is_enemy:
        person = {'name': get_random_name()}
        person.update({'clas': random.choice(list(classes))})
        person.update({'name': get_random_name()})
    else:
        rol = input('Введите цифру 1 - Warrior, 2 - Ranger, 3 - Mage, 4 - Healer, 5 - Assasin\n')
        person = {'name': get_player_name()}
        person.update({'clas': role[rol]})
        person.update({'char': classes[person['clas']]})
        print(f"{person['name']} - {person['clas']}, имеет характеристики: {person['char']}")
        return person


def get_player_name() -> str:
    player_name = ''
    while player_name == '':
        player_name = input('Как зовут твоего персонажа\n')
    return player_name


def get_random_name() -> str:
    firstname = random.choice(first_name)
    secondname = random.choice(second_name)
    name = f'{firstname} {secondname}'
    return name


Player1 = init_person(False)
Player2 = init_person(False)


def use_shield(player):
    if player['char']['uses']['shield']['kd'] != 0:
        print("It's not time to shut up!")
        return False
    elif player['char']['armor'] == 10:
        player['char']['hp'] += 5
        print(f"{player['name']} has too many shields that we heal him on 5 hp")
    else:
        player['char']['armor'] += player['char']['uses']['shield']['power']
        print(f"{player['name']} use shield and increase his armor by 1")
        player['char']['uses']['shield']['kd'] = 2


def use_xhit(player):
    if player['char']['uses']['xhit']['kd'] != 0:
        print("Shhhhhh, it's not time")
    else:
        player['char']['attack'] += player['char']['uses']['xhit']['power']
        print(f"{player['name']} use xhit and increase his attack by 1")
        player['char']['uses']['xhit']['kd'] = 2


def use_fireball(player, enemy):
    if player['char']['uses']['fireball']['kd'] != 0:
        print("Hahaha, I can't use it now")
    else:
        enemy['char']['hp'] -= player['char']['uses']['fireball']['power']
        print(f"{player['name']} use fireball and deal 18 damage to {enemy['name']}")
        player['char']['uses']['fireball']['kd'] = 3


def use_heal(player):
    if player['char']['uses']['heal']['kd'] != 0:
        print("Sorry, but I can't heal now")
    else:
        player['char']['hp'] += player['char']['uses']['heal']['power']
        print(f"{player['name']} use heal")
        player['char']['uses']['heal']['kd'] = 3


def use_skill(player1, player2):
    if player1['clas'] == 'Warrior':
        if player1['char']['uses']['shield']['kd'] != 0:
            print("I should attack")
            damage = player1['char']['attack'] - player2['char']['armor']
            if damage < 0:
                damage = 0
            player2['char']['hp'] -= damage
            print(f"{player1['name']} attack {player2['name']} and deal {damage} damage")
        else:
            use_shield(player1)
    elif player1['clas'] == 'Ranger':
        if player1['char']['uses']['xhit']['kd'] != 0:
            print("I should attack")
            damage = player1['char']['attack'] - player2['char']['armor']
            if damage < 0:
                damage = 0
            player2['char']['hp'] -= damage
            print(f"{player1['name']} attack {player2['name']} and deal {damage} damage")
        else:
            use_xhit(player1)
    elif player1['clas'] == 'Mage':
        if player1['char']['uses']['fireball']['kd'] != 0:
            print("I should attack")
            damage = player1['char']['attack'] - player2['char']['armor']
            if damage < 0:
                damage = 1
            player2['char']['hp'] -= damage
            print(f"{player1['name']} attack {player2['name']} and deal {damage} damage")
        else:
            use_fireball(player1, player2)
    elif player1['clas'] == 'Healer':
        if player1['char']['uses']['heal']['kd'] != 0:
            print("I should attack")
            damage = player1['char']['attack'] - player2['char']['armor']
            if damage < 0:
                damage = 0
            player2['char']['hp'] -= damage
            print(f"{player1['name']} attack {player2['name']} and deal {damage} damage")
        else:
            use_heal(player1)


def attack_by_assasin(player1, player2):
    chance = random.randint(1, 100)
    if chance > player1['char']['uses']['crit']['chance']:
        damage = player1['char']['attack'] - player2['char']['armor']
        if damage < 0:
            damage = 0
        player2['char']['hp'] -= damage
        print(f"{player1['name']} attack {player2['name']} and deal {damage} damage")
    else:
        damage = player1['char']['attack'] * player1['char']['uses']['crit']['power'] - player2['char']['armor']
        if damage < 0:
            damage = 0
        player2['char']['hp'] -= damage
        player1['char']['uses']['crit']['chance'] += 5
        print(f"{player1['name']} attack {player2['name']} and deal {damage} critical damage")


def fight(player1, player2):
    print(cyan + f"It's time to {player1['name']} to start")
    if player1['clas'] == 'Assasin':
        attack_by_assasin(player1, player2)
    else:
        if player1['clas'] == 'Warrior':
            if player1['char']['uses']['shield']['kd'] != 0:
                player1['char']['uses']['shield']['kd'] -= 1
        elif player1['clas'] == 'Ranger':
            if player1['char']['uses']['xhit']['kd'] != 0:
                player1['char']['uses']['xhit']['kd'] -= 1
        elif player1['clas'] == 'Mage':
            if player1['char']['uses']['fireball']['kd'] != 0:
                player1['char']['uses']['fireball']['kd'] -= 1
        elif player1['clas'] == 'Healer':
            if player1['char']['uses']['heal']['kd'] != 0:
                player1['char']['uses']['heal']['kd'] -= 1
        choose = int(input(f"You can 1 - attack, 2 - use {player1['char']['uses']}\n"))
        if choose == 1:
            damage = player1['char']['attack'] - player2['char']['armor']
            if damage < 0:
                damage = 0
            player2['char']['hp'] -= damage
            print(cyan + f"{player1['name']} attack {player2['name']} and deal {damage} damage")
        elif choose == 2:
            use_skill(player1, player2)
    print(blue + f"{player2['name']}'s hp is {player2['char']['hp']}")
    print("Use пробел to do the next attack")
    keyboard.wait(' ')
    clear()
    print(blue + f"It's time to {player2['name']} to start")
    if player2['clas'] == 'Assasin':
        attack_by_assasin(player2, player1)
    else:
        if player2['clas'] == 'Warrior':
            if player2['char']['uses']['shield']['kd'] != 0:
                player2['char']['uses']['shield']['kd'] -= 1
        elif player2['clas'] == 'Ranger':
            if player2['char']['uses']['xhit']['kd'] != 0:
                player2['char']['uses']['xhit']['kd'] -= 1
        elif player2['clas'] == 'Mage':
            if player2['char']['uses']['fireball']['kd'] != 0:
                player2['char']['uses']['fireball']['kd'] -= 1
        elif player2['clas'] == 'Healer':
            if player2['char']['uses']['heal']['kd'] != 0:
                player2['char']['uses']['heal']['kd'] -= 1
        choose = int(input(f"You can 1 - attack, 2 - use {player2['char']['uses']}\n"))
        if choose == 1:
            damage = player2['char']['attack'] - player1['char']['armor']
            if damage < 0:
                damage = 0
                player1['char']['hp'] -= damage
            print(blue + f"{player2['name']} attack {player1['name']} and deal {damage} damage")
        elif choose == 2:
            use_skill(player2, player1)
    print(cyan + f"{player1['name']}'s hp is {player1['char']['hp']}")
    print("Use пробел to do the next attack")
    keyboard.wait(' ')
    clear()


for i in range(20):
    fight(Player1, Player2)
    if Player1['char']['hp'] < 1 or Player2['char']['hp'] < 1:
        break


if Player1['char']['hp'] > 0 and Player2['char']['hp'] < 1:
    print(f"{Player1['name']} Win")
if Player1['char']['hp'] < 1 and Player2['char']['hp'] > 0:
    print(f"{Player2['name']} Win")
if Player1['char']['hp'] < 1 and Player2['char']['hp'] < 1:
    print(f"Winner, winner, friendly dinner")
if Player1['char']['hp'] > 0 and Player2['char']['hp'] > 0:
    if Player1['char']['hp'] > Player2['char']['hp']:
        print(f"{Player1['name']} Win")
    else:
        print(f"{Player2['name']} Win")
print("Finish")
keyboard.wait(' ')
