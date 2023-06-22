import random
import yaml
from calendar import monthrange


with open('../backend/config.yml', 'r', encoding='utf8') as file:
    cfg = yaml.safe_load(file)

# =============================

km_needed = (cfg['last_day_value'] - cfg['first_day_value'])
rows_needed = km_needed // random.randint(cfg['dayly_min'], cfg['dayly_max'])

# check if it is out of range
# if it is, sets extreme values
if rows_needed < cfg['min_days']:
    rows_needed = cfg['min_days']
if rows_needed > cfg['max_days']:
    rows_needed = cfg['max_days']

# =============================
num_days = monthrange(cfg['year'], cfg['month'],)[1]
dates = sorted(random.sample(range(1, num_days + 1), rows_needed))

# =============================


def generate_distances(monthly_distance = km_needed, days_quantity = rows_needed, min = cfg['dayly_min'], max = cfg['dayly_max']):

    distance_left = monthly_distance
    distances = []

    for _ in range(days_quantity):
        r = random.randint(min, max)
        distance_left -= r
        distances.append(r)

    if distance_left > 0:
        add_all = int(distance_left / days_quantity) 
        add_rest = distance_left - (add_all * days_quantity)
        for i in range(len(distances)):
            distances[i] += add_all
        
        for n in range(add_rest):
            distances[n] += 1
        return distances
    elif distance_left < 0:
        add_all = int(distance_left / days_quantity) * -1
        add_rest = (distance_left * -1) - (add_all * days_quantity)
        for i in range(len(distances)):
            distances[i] -= add_all
        
        for n in range(add_rest):
            distances[n] -= 1
        return distances
    else:
        return distances
