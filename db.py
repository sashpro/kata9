reg_food_name = '[A-Z]'
reg_kg= '(\d+\.)?\d+'

qtype = {'pcs': {'format': reg_food_name, 'add': 1}, 'kg': {'format': reg_food_name+reg_kg, 'add': reg_kg}}


food = {'A': {'price': 0.5, 'qtype': 'pcs'},
        'B': {'price': 0.3, 'qtype': 'pcs'},
        'C': {'price': 1.99, 'qtype': 'kg'},
        'D': {'price': 1.2, 'qtype': 'pcs'},
        'E': {'price': 0.9, 'qtype': 'pcs'},

        }

discount = {
    'A': {'quantity': 3, 'discount': 1.3, 'bonus': None},
    'B': {'quantity': 2, 'discount': 0.45, 'bonus': None},
    'D': {'quantity': 2, 'discount': 0, 'bonus': 'E'},

}
