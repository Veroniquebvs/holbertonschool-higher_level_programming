#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {key: value * 2 for key, value in a_dictionary.items()}
    return new_dict


# prix_euros = {"pomme": 1.5, "banane": 0.8, "orange": 2.0}
# Convertir en dollars (taux 1.1)
# prix_dollars = {fruit: prix * 1.1 for fruit, prix in prix_euros.items()}
# print(prix_dollars)  # {'pomme': 1.65, 'banane': 0.88, 'orange': 2.2}
