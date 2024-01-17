spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    name_list = [food["name"] for food in spicy_foods]
    return name_list
    

def get_spiciest_foods(spicy_foods):
    big_spice = [food for food in spicy_foods if food["heat_level"] > 5]
    return big_spice
    pass

def print_spicy_foods(spicy_foods):
    for f in spicy_foods:
        name = f["name"]
        cuis = f["cuisine"]
        heat = f["heat_level"]
        emojis = "🌶" * heat
        print(f"{name} ({cuis}) | Heat Level: {emojis}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for f in spicy_foods:
        if f["cuisine"] == cuisine:
            return f

def print_spiciest_foods(spicy_foods):
    big_spice = [f for f in spicy_foods if f["heat_level"] > 5]
    for bs in big_spice:
        name = bs["name"]
        cuis = bs["cuisine"]
        heat = bs["heat_level"]
        emoj = "🌶" * heat
        print(f"{name} ({cuis}) | Heat Level: {emoj}")

def get_average_heat_level(spicy_foods):
    all_heat = 0
    for f in spicy_foods:
        all_heat += f["heat_level"]
    avg = all_heat / len(spicy_foods)
    return int(avg)
    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods


