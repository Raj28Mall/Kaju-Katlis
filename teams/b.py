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
    logic(arena_data)
    return deploy_list.list_, team_signal

def choose_troop(enemy_tanks, enemy_dps, enemy_swarm, deployable):
    """Decide the best troop to deploy based on enemy composition."""
    TANK=["Giant","Valkyrie", "Prince", "Knight"]
    DPS=["Musketeer","Wizard","Balloon", "Archer"]
    SWARM=["Skeleton","Minion","Barbaraian", "Dragon"]
    if enemy_tanks > enemy_dps and enemy_tanks > enemy_swarm:
        return select_best(DPS, deployable)
    elif enemy_dps > enemy_swarm:
        return select_best(SWARM, deployable)  
    else:
        return select_best(TANK, deployable)
    
def select_best(category, deployable):
    # Actually we would have weight based system for troop selection in this
    TANK=["Giant","Valkyrie", "Prince", "Knight"]
    DPS=["Musketeer","Wizard","Balloon", "Archer"]
    SWARM=["Skeleton","Minion","Barbaraian", "Dragon"]
    for i in range(0,4):
        if category[i] in deployable:
            return category[i]
    

def logic(arena_data: dict):
    global team_signal
    my_tower = arena_data["MyTower"]
    opp_troops = arena_data["OppTroops"]
    TANK=["Giant","Valkyrie", "Prince", "Knight"]
    DPS=["Musketeer","Wizard","Balloon", "Archer"]
    SWARM=["Skeleton","Minion","Barbaraian", "Dragon"]

    tokens = [token.strip().title() for token in team_signal.split(",") if token.strip() != "h"]
    
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

    troop_to_deploy = choose_troop(enemy_tanks, enemy_dps, enemy_swarm, my_tower.deployable_troops)
    deploy_list.list_.append((troop_to_deploy, (random_x(-10, 10), 0)))
