import random

roles = ['Mafia', 'Detective', 'Doctor', 'Villager', 'Villager']
players = {}


def assign_roles(participants):
    shuffled_roles = roles[:]
    random.shuffle(shuffled_roles)
    for i, participant in enumerate(participants):
        players[participant] = shuffled_roles[i]
        # send_private_message would be called here
    return players
