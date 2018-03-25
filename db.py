reg_food_name = '[A-Z]'
reg_kg= '(\d+\.)?\d+'

qtype = {'pcs': {'format': reg_food_name, 'add': 1}, 'kg': {'format': reg_food_name+reg_kg, 'add': reg_kg}}

food = {'A': {'price': 1, 'qtype': 'pcs'},
        'B': {'price': 2, 'qtype': 'pcs'},
        'C': {'price': 2, 'qtype': 'kg'}
        }

discount = {
    'A': {'quantity': 2, 'discount': 1.5, 'bonus': None},
    'B': {'quantity': 2, 'discount': 3, 'bonus': None},
    'C': {'quantity': 2, 'discount': 0, 'bonus': 'A'},
}
