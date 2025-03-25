import random
from teams.helper_function import Troops, Utils

"giant, balloon, wizard, musketeer, valkyrie, minion, barbarian, skeleton"

team_name = "Kaju Katlis"
troops = [Troops.giant, Troops.balloon, Troops.wizard, Troops.musketeer,Troops.valkyrie, Troops.minion, Troops.barbarian, Troops.skeleton]

deploy_list = Troops([])
team_signal = "h"

def random_x(min_val=-25, max_val=25):
    return random.randint(min_val, max_val)

def deploy(arena_data: dict):
    """
    Custom deploy function that prioritizes a ground push with Valkyrie.
    It dynamically updates `team_signal` to reflect detected enemy troops 
    (without breaking formatting).
    
    Returns:
        deploy_list (list): A list of tuples (troop, (x, y) deploy position).
        team_signal (str): Updated team signal.
    """
    logic(arena_data)
    return deploy_list.list_, team_signal

def choose_troop(enemy_tanks, enemy_dps, enemy_swarm):
    """Decide the best troop to deploy based on enemy composition."""
    TANK=["giant","valkyrie", "prince", "knight"]
    DPS=["musketeer","wizard","balloon", "archer"]
    SWARM=["skeleton","minion","barbaraian", "dragon"]
    if enemy_tanks > enemy_dps and enemy_tanks > enemy_swarm:
        return select_best(DPS)
    elif enemy_dps > enemy_swarm:
        return select_best(SWARM)  
    else:
        return select_best(TANK)
    
def select_best(category):
    # Actually we would have weight based system for troop selection in this
    TANK=["giant","valkyrie", "prince", "knight"]
    DPS=["musketeer","wizard","balloon", "archer"]
    SWARM=["skeleton","minion","barbaraian", "dragon"]
    if category == "TANK":
        return category[0]
    elif category == "DPS":
        return category[0]
    else:
        return category[0]
    

def logic(arena_data: dict):
    global team_signal
    my_tower = arena_data["MyTower"]
    opp_troops = arena_data["OppTroops"]

    TANK=["giant","valkyrie", "prince", "knight"]
    DPS=["musketeer","wizard","balloon", "archer"]
    SWARM=["skeleton","minion","barbaraian", "dragon"]

    tokens = [token.strip().lower() for token in team_signal.split(",") if token.strip() != "h"]
    
    for troop in opp_troops:
        if troop.name.lower() not in tokens:
            tokens.append(troop.name.lower())
    
    tokens = tokens[-4:]
    team_signal = "h, " + ", ".join(tokens)

    enemy_tanks = sum(1 for token in tokens if token in TANK)
    enemy_dps   = sum(1 for token in tokens if token in DPS)
    enemy_swarm = sum(1 for token in tokens if token in SWARM)

    current_names = [name.strip() for name in team_signal.split(",")] if team_signal else []
    for troop in opp_troops:
        if troop.name not in current_names:
            current_names.append(troop.name)  

    team_signal = ", ".join(["h"] + [name for name in current_names if name != "h"])

    troop_to_deploy = choose_troop(enemy_tanks, enemy_dps, enemy_swarm)
    deploy_list.list_.append((troop_to_deploy, (random_x(-10, 10), 0)))
