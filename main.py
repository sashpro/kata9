import re
from db import food, qtype, discount
from typing import Dict, Tuple
from collections import defaultdict


def parse_basket(fstr: str) -> Dict:
    result_basket = defaultdict(lambda: 0)
    mres=1
    while mres:
        current_food = fstr[0]
        quantity_type = food[current_food]['qtype']
        mres = re.match(qtype[quantity_type]['format'], fstr)
        if mres:
            food_abbr = mres.group(0)
            fstr = fstr[len(food_abbr):]
            inc = qtype[quantity_type]['add']
            result_basket[current_food] += inc if isinstance(inc, int) else float(re.search(inc, food_abbr).group(0))
            if len(fstr) == 0:
                break
    return result_basket


def apply_discount(**parsed_basket: Dict) -> Tuple[float, Dict, Dict]:
    total = 0
    bonus_foods = defaultdict(lambda: 0)
    for disc, value in parsed_basket.items():
        if disc not in discount:
            total += food[disc]['price']*value
            continue
        value = discount[disc]
        amount = parsed_basket[disc]
        bonus_mul = 0
        if amount >= value['quantity']:
            bonus_mul = amount // value['quantity']
            if value.get('discount'):
                amount = amount % value['quantity']
            if value['bonus']:
                bonus_foods[value['bonus']] += bonus_mul
        print(food[disc]['price'],amount)
        total += food[disc]['price']*amount + bonus_mul*value['discount']
    return total, parsed_basket, dict(bonus_foods)

a = input('enter foods: ')
bres = parse_basket(a)
print("total: {}, basket - {}, bonuses - {}".format(*apply_discount(**bres)))
